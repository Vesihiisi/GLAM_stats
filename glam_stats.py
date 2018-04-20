# !/usr/bin/python
# -*- coding: utf-8 -*-
"""Save usage stats for selected GLAM categories.

Usage: python3 glam_stats.py --config se_config.json
"""
from datetime import datetime
from lxml import etree
import argparse
import json
import requests


def generate_filename():
    return datetime.today().strftime('%Y-%m-%d')


def make_url(catname):
    base = (
        "https://tools.wmflabs.org//glamtools/glamorous.php"
        "?doit=1&category={}"
        "&use_globalusage=1&ns0=1&depth=9&projects[wikipedia]=1"
        "&projects[wikimedia]=1&projects[wikisource]=1"
        "&projects[wikibooks]=1&projects[wikiquote]=1"
        "&projects[wiktionary]=1&projects[wikinews]=1"
        "&projects[wikivoyage]=1&projects[wikispecies]=1"
        "&projects[mediawiki]=1&projects[wikidata]=1"
        "&projects[wikiversity]=1&format=xml"
    )
    return base.format(catname.replace(" ", "+"))


def calculate_percent(part, whole):
	if float(whole) > 0:
		return round(100 * float(part) / float(whole), 2)
	else:
		return 0


def process_data(xmlblob):
    row = {}
    tree = etree.fromstring(xmlblob)
    no_files = tree.get("images_in_category")
    row["files"] = no_files
    for child_of_root in tree:
        distinct_used = child_of_root.get("distinct_images")
        row["percent_used"] = calculate_percent(distinct_used, no_files)
        row["total_usage"] = child_of_root.get("total_usage")
        row["distinct_used"] = distinct_used
    return row


def analyze_single(item):
    url = make_url(item["cat"])
    data = download_data(url)
    row = process_data(data)
    row["name"] = item["name"]
    row["cat"] = item["cat"].replace(" ", "_")
    return row


def download_data(url):
    return requests.get(url).text


def read_json_file(fname):
    return json.load(open(fname))


def save_file(fname, txt):
    with open(fname, 'w') as f:
        f.write(txt)
        print("Saved file: {}".format(fname))


def save_json_file(fname, data):
    with open(fname, 'w') as f:
        json.dump(data, f,
                  ensure_ascii=False,
                  sort_keys=True, indent=4)
        print("Saved file: {}".format(fname))


def make_wikitable(data):
    txt = '{| class="wikitable sortable"\n|-\n'
    txt += "! {}\n".format("institution")
    txt += "! {}\n".format("files")
    txt += "! {}\n".format("used")
    txt += "! {}\n".format("% used")
    for r in data:
        link_base = "[[:commons:Category:{}|{}]]"
        link = link_base.format(r["cat"], r["name"])
        txt += "|-\n"
        txt += "| {}\n".format(link)
        txt += "| {}\n".format(r["files"])
        txt += "| {}\n".format(r["distinct_used"])
        txt += "| {}\n".format(r["percent_used"])
    txt += "|}\n"
    return txt


def make_markdown(data):
    txt = "| {} | {} | {} | {} |\n".format("institution",
                                           "files",
                                           "used",
                                           "% used")
    txt += "|---|---|---|---|\n"
    for r in data:
        link_base = "https://commons.wikimedia.org/wiki/Category:{}"
        link_str = link_base.format(r["cat"])
        link = "[{}]({})".format(r["name"], link_str)
        txt += "| {} | {} | {} | {} |\n".format(link,
                                                r["files"],
                                                r["distinct_used"],
                                                r["percent_used"])
    return txt


def extract_number_files(json):
    return int(json["files"])


def save_processed(rows):
    fname = generate_filename()
    save_json_file("{}.json".format(fname), rows)
    save_file("{}.md".format(fname), make_markdown(rows))
    save_file("{}.wiki".format(fname), make_wikitable(rows))


def main(f_config):
    cats = read_json_file(f_config)
    message = "[{}] I'm going to analyze {} cats...🐈"
    print(message.format(f_config, len(cats)))
    rows = []
    for cat in cats:
        rows.append(analyze_single(cat))
    rows.sort(key=extract_number_files, reverse=True)
    save_processed(rows)


if __name__ == "__main__":
    arguments = {}
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",
                        help='file with categories to analyze',
                        default="se_config.json")
    args = parser.parse_args()
    main(args.config)
