#!/usr/bin/env python3
"""Write a coverage badge SVG from a percentage, PHPUnit clover.xml, or lcov.info.

The badge is red below 50, yellow below 80, and green from 80 up. Unknown or
empty input uses a neutral color and the label "n/a". This script does not
commit, push, or contact GitHub. The calling workflow decides when to commit
the SVG (only on the default branch, only when the file changed, with
[skip ci] in the commit message).
"""

import argparse
import math
import os
import sys
import xml.etree.ElementTree as ET


NEUTRAL = '#9f9f9f'
RED = '#e05d44'
YELLOW = '#dfb317'
GREEN = '#4c1'


def text_width(text):
    return int(len(text) * 6.5) + 12


def badge_color(percent):
    if percent is None:
        return NEUTRAL
    if percent < 50:
        return RED
    if percent < 80:
        return YELLOW
    return GREEN


def rounded_percent(percent):
    return int(math.floor(percent + 0.5))


def badge_label(percent):
    if percent is None:
        return 'n/a'
    return f'{rounded_percent(percent)}%'


def badge_svg(value_text, color):
    label = 'coverage'
    label_width = text_width(label)
    value_width = text_width(value_text)
    total = label_width + value_width
    label_x = int(round(label_width / 2 * 10))
    value_x = int(round((label_width + value_width / 2) * 10))
    title = f'coverage: {value_text}'
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{total}" height="20" role="img" aria-label="{title}">\n'
        f'<title>{title}</title>\n'
        '<linearGradient id="coverage-smooth" x2="0" y2="100%">\n'
        '<stop offset="0" stop-color="#bbb" stop-opacity=".1"/>\n'
        '<stop offset="1" stop-opacity=".1"/>\n'
        '</linearGradient>\n'
        '<clipPath id="coverage-round">\n'
        f'<rect width="{total}" height="20" rx="3" fill="#fff"/>\n'
        '</clipPath>\n'
        '<g clip-path="url(#coverage-round)">\n'
        f'<rect width="{label_width}" height="20" fill="#555"/>\n'
        f'<rect x="{label_width}" width="{value_width}" height="20" fill="{color}"/>\n'
        f'<rect width="{total}" height="20" fill="url(#coverage-smooth)"/>\n'
        '</g>\n'
        '<g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" '
        'text-rendering="geometricPrecision" font-size="110">\n'
        f'<text aria-hidden="true" x="{label_x}" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)">{label}</text>\n'
        f'<text x="{label_x}" y="140" transform="scale(.1)">{label}</text>\n'
        f'<text aria-hidden="true" x="{value_x}" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)">{value_text}</text>\n'
        f'<text x="{value_x}" y="140" transform="scale(.1)">{value_text}</text>\n'
        '</g>\n'
        '</svg>\n'
    )


def ratio(covered, total):
    if covered is None or total is None:
        return None
    total_n = float(total)
    if total_n <= 0:
        return None
    return float(covered) / total_n * 100.0


def local_name(tag):
    return tag.rsplit('}', 1)[-1]


def percentage_from_clover(path):
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        raise SystemExit(f'Could not parse clover XML {path}: {exc}') from exc

    project = root if local_name(root.tag) == 'project' else None
    if project is None:
        for element in root.iter():
            if local_name(element.tag) == 'project':
                project = element
                break
    if project is None:
        raise SystemExit(f'Clover file {path} has no project element')

    metrics = None
    for child in list(project):
        if local_name(child.tag) == 'metrics':
            metrics = child
            break
    if metrics is None:
        raise SystemExit(f'Clover file {path} has no project metrics')

    percent = ratio(metrics.get('coveredstatements'), metrics.get('statements'))
    if percent is None:
        percent = ratio(metrics.get('coveredelements'), metrics.get('elements'))
    return percent


def percentage_from_lcov(path):
    lines_found = 0
    lines_hit = 0
    saw_record = False
    with open(path, 'r', encoding='utf-8') as handle:
        for line in handle:
            if line.startswith('LF:'):
                lines_found += int(line[3:].strip() or 0)
                saw_record = True
            elif line.startswith('LH:'):
                lines_hit += int(line[3:].strip() or 0)
                saw_record = True
    if not saw_record or lines_found <= 0:
        return None
    return lines_hit / lines_found * 100.0


def bounded(percent):
    if percent is None:
        return None
    if not math.isfinite(percent) or percent < 0 or percent > 100:
        raise SystemExit('percentage must be between 0 and 100')
    return percent


def parse_args(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--percent', type=float, help='Coverage percentage from 0 to 100.')
    source.add_argument('--clover', help='Path to a PHPUnit clover.xml report.')
    source.add_argument('--lcov', help='Path to an lcov.info report.')
    parser.add_argument(
        '--output',
        default='.github/badges/coverage.svg',
        help='SVG path to write (default: .github/badges/coverage.svg).',
    )
    return parser.parse_args(argv)


def percentage_from_args(args):
    if args.percent is not None:
        return bounded(args.percent)
    path = args.clover or args.lcov
    if not os.path.isfile(path):
        raise SystemExit(f'Coverage report not found: {path}')
    if args.clover:
        return bounded(percentage_from_clover(path))
    return bounded(percentage_from_lcov(path))


def main(argv):
    args = parse_args(argv)
    percent = percentage_from_args(args)
    shown = badge_label(percent)
    # Color follows the integer drawn on the badge. Unknown input stays neutral.
    color_source = None if percent is None else rounded_percent(percent)
    svg = badge_svg(shown, badge_color(color_source))
    destination = args.output
    parent = os.path.dirname(destination)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(destination, 'w', encoding='utf-8') as handle:
        handle.write(svg)
    print(f'wrote {destination} ({shown})')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
