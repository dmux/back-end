# -*- coding: utf-8 -*-
import re
from .models import (
    Card,
    CardRow,
)

regex_dict = {
    'row': re.compile(r'(?P<row>C+([\d])+\s+\d{0,51})'),
}


def _parse_line(line):
    for key, rx in regex_dict.items():
        match = rx.search(line)
        if match:
            return key, match
    return None, None


def parser(filepath):
    data_row = []

    with open(filepath, 'r') as file_object:
        line = file_object.readline()
        name = line[0:29]
        date = line[29:37]
        batch = line[37:45]
        qty_records = line[45:51]

        card = Card.objects.create(
            name=name,
            date=date,
            batch=batch,
            qty_records=qty_records,
        )

        while line:
            key, match = _parse_line(line)
            if key == 'row':
                row = match.group('row')
                row_tag = row[0:1]
                row_batch = row[1:7]
                row_card = row[8:26]

                row = {
                    'row_tag': row_tag,
                    'row_batch': row_batch,
                    'row_card': row_card,
                }

                data_row.append(row)

            line = file_object.readline()

        for i in data_row:
            CardRow.objects.create(
                card=card,
                tag=i['row_tag'],
                batch=i['row_batch'],
                number=i['row_card'],
            )
