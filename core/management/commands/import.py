from django.core.management.base import BaseCommand

from core.engine import ImportDataFromCSV


class Command(BaseCommand):
    """
    Import csv data

    Usage
        $ python manage.py import --file <location of .csv>
    """

    help = "Import CSV from SP Fairs data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            dest="file",
            help="CSV Location.",
        )

    def handle(self, *args, **options):
        file = options["file"]
        assert file, "CSV location must be defined. Type manage.py import help"
        self.stdout.write("Importing...")
        import_cmd = ImportDataFromCSV()
        created_fair = import_cmd.read_data(file)
        self.stdout.write(
            "Done! Imported {lines} lines".format(lines=len(created_fair))
        )
