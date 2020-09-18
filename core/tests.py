import time

from django.test import TestCase

from mb.settings.utils import get_env_var

from .engine import ImportDataFromCSV

from .models import Fair
from district.models import District
from subprefecture.models import SubPrefecture
from zone.models import Zone8, Zone5


class TestEngine(TestCase):
    def setUp(self):
        self.import_cmd = ImportDataFromCSV()
        self.csv_content = [
            [
                "ID",
                "LONG",
                "LAT",
                "SETCENS",
                "AREAP",
                "CODDIST",
                "DISTRITO",
                "CODSUBPREF",
                "SUBPREFE",
                "REGIAO5",
                "REGIAO8",
                "NOME_FEIRA",
                "REGISTRO",
                "LOGRADOURO",
                "NUMERO",
                "BAIRRO",
                "REFERENCIA",
            ],
            [
                "1",
                "-46550164",
                "-23558733",
                "355030885000091",
                "3550308005040",
                "87",
                "VILA FORMOSA",
                "26",
                "ARICANDUVA-FORMOSA-CARRAO",
                "Leste",
                "Leste 1",
                "VILA FORMOSA",
                "4041-0",
                "RUA MARAGOJIPE",
                "S/N",
                "VL FORMOSA",
                "TV RUA PRETORIA",
            ],
        ]

    def test_csv_import_file(self):
        file = ".data/TEST_DEINFO_AB_FEIRASLIVRES_2014_1_LINE.csv"
        self.import_cmd.read_data_from_csv(file)
        self.assertEqual(self.csv_content, self.import_cmd.csv_data)

    def test_load_data_from_obj(self):
        file = ".data/TEST_DEINFO_AB_FEIRASLIVRES_2014_1_LINE.csv"
        created_fair = self.import_cmd.read_data(file)
        self.assertEqual(len(created_fair), 1)


class TestAPI(TestCase):
    def setUp(self):
        self.API_URL = "{default_url}/v1".format(
            default_url=get_env_var("DEFAULT_URL", "")
        )
        self.zone_5 = Zone5.objects.create(name="Oeste")
        self.zone_8 = Zone8.objects.create(name="Oeste II", zone_5=self.zone_5)
        self.sub_prefecture = SubPrefecture.objects.create(
            name="Sub. Prefeitura Zona Oeste", zone_8=self.zone_8
        )
        self.district = District.objects.create(
            name="Sumarezinho", sub_prefecture=self.sub_prefecture
        )
        self.fair = Fair.objects.create(
            district=self.district,
            name="Sao Joaquim",
            longitude=-32.123456,
            latitude=-32.123456,
            setcens="0123456789",
            area="0123456789",
            register="0000-1",
            street="Rua Sao Joaquim",
            number="S/N",
            neighborhood="Sao Joaquim",
            reference="Caixa D'agua",
        )

    def test_has_default_url(self):
        self.assertNotEqual(self.API_URL, "/v1")

    def test_list(self):
        time.sleep(1)
        list_url = "{API_URL}/fair/".format(API_URL=self.API_URL)
        response = self.client.get(list_url)
        self.assertEqual(int(response.status_code), 200)

    def test_create(self):
        time.sleep(1)
        create_url = "{API_URL}/fair/create/".format(API_URL=self.API_URL)
        fair_data = {
            "district": 1,
            "name": "Teste de Feira",
            "longitude": -32.123456,
            "latitude": -32.123456,
            "setcens": "0123456789",
            "area": "0123456789",
            "register": "0000-1",
            "street": "Rua Teste",
            "number": "123",
            "neighborhood": "Bairro Teste",
            "reference": "",
        }
        response = self.client.post(create_url, data=fair_data)
        self.assertEqual(int(response.status_code), 201)

    def test_update(self):
        time.sleep(1)
        update_url = "{API_URL}/fair/{fair_id}/".format(
            API_URL=self.API_URL, fair_id=self.fair.id
        )
        fair_data = {
            "name": "Teste de Feira",
            "longitude": -32.123456,
            "latitude": -32.123456,
            "setcens": "0123456789",
            "area": "0123456789",
            "register": "0000-1",
            "street": "Rua Teste",
            "number": "123",
            "neighborhood": "Bairro Teste",
            "reference": "",
        }
        response = self.client.patch(
            update_url, data=fair_data, content_type="application/json"
        )
        self.assertEqual(int(response.status_code), 200)

    def test_delete(self):
        time.sleep(1)
        delete_url = "{API_URL}/fair/{fair_id}/".format(
            API_URL=self.API_URL, fair_id=self.fair.id
        )
        response = self.client.delete(delete_url)
        self.assertEqual(int(response.status_code), 204)
