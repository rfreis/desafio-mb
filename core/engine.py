import csv

from decimal import Decimal

from .models import Fair

from district.models import District

from subprefecture.models import SubPrefecture

from zone.models import Zone5, Zone8


class ImportDataFromCSV:
    fair_fields = {
        "id": 0,
        "longitude": 1,
        "latitude": 2,
        "setcens": 3,
        "area": 4,
        "name": 11,
        "register": 12,
        "street": 13,
        "number": 14,
        "neighborhood": 15,
        "reference": 16,
    }
    district_fields = {
        "id": 5,
        "name": 6,
    }
    sub_prefecture_fields = {
        "id": 7,
        "name": 8,
    }
    zone_5_fields = {
        "name": 9,
    }
    zone_8_fields = {
        "name": 10,
    }

    def read_data(self, file):
        self.read_data_from_csv(file)
        created_fair = self.load_data_from_obj()
        return created_fair

    def read_data_from_csv(self, csv_file):
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            data_from_csv = list(reader)
        self.csv_data = data_from_csv

    def load_data_from_obj(self):
        created_fair = []
        csv_data = self.csv_data
        for index, line in enumerate(csv_data):
            if index:
                fair = self.load_line_from_obj(line)
                created_fair.append(fair)
        return created_fair

    def load_line_from_obj(self, line):
        data_structure = [
            {
                "MyModel": Fair,
                "default_fields": self.fair_fields,
            },
            {
                "MyModel": District,
                "default_fields": self.district_fields,
                "field_name": "district",
            },
            {
                "MyModel": SubPrefecture,
                "default_fields": self.sub_prefecture_fields,
                "field_name": "sub_prefecture",
            },
            {
                "MyModel": Zone8,
                "default_fields": self.zone_8_fields,
                "field_name": "zone_8",
            },
            {
                "MyModel": Zone5,
                "default_fields": self.zone_5_fields,
                "field_name": "zone_5",
            },
        ]
        _, fair = self.load_object(data_structure, line)
        return fair

    def load_lat_or_long_value(self, raw_value):
        decimal_value = Decimal(raw_value) / 1000000
        return decimal_value

    def load_object(self, data_structure, line):
        fields_with_data = {}
        data_item = data_structure.pop(0)
        if data_structure:
            field_name, instance = self.load_object(data_structure, line)
            if field_name and instance:
                fields_with_data[field_name] = instance
        obj = self.get_or_create_object(
            data_item["MyModel"],
            data_item["default_fields"],
            line,
            fields_with_data,
        )
        if "field_name" in data_item:
            field_name = data_item["field_name"]
            return field_name, obj
        return None, obj

    def get_or_create_object(
        self, MyModel, default_fields, line, fields_with_data
    ):
        for field_name, position in default_fields.items():
            try:
                value = line[position]
            except IndexError:
                value = None
            if field_name in ("longitude", "latitude"):
                value = self.load_lat_or_long_value(value)
            if field_name in ("setcens", "area"):
                value = int(value)
            if value:
                fields_with_data[field_name] = value
        obj, created = MyModel.objects.get_or_create(**fields_with_data)
        return obj
