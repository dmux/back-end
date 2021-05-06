# Documentação da API do Backend - Desafio Hyperativa

## Dependências do Projeto

- Python 3.8+
- Django 3.1.9+
- Uses [Poetry](https://python-poetry.org/) - the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn.
- PostgreSQL database support with psycopg2-binary.
- Uses [Django Searchable Encrypted Fields](https://pypi.org/project/django-encrypted-model-fields/).
- Uses [Django REST framework](http://www.django-rest-framework.org/) - is a powerful and flexible toolkit for building Web APIs.
- Uses [DRF API Logger](https://pypi.org/project/drf-api-logger/).

## Dependências Produção

- [Graphviz](https://www.graphviz.org/)
- [Python 3.8.9](https://www.python.org/downloads/release/python-389/)

## Dependências Desenvolvimento

- build-essential
- cmake
- git
- libopenblas-dev
- liblapack-dev
- libx11-dev
- libgtk-3-dev
- libpq-dev
- curl
- wget
- vim
- gettext
- locales
- libmemcached-dev
- zlib1g-dev
- latexmk
- texlive
- texlive-science
- texlive-formats-extra
- texlive-latex-recommended
- texlive-latex-extra
- texlive-fonts-recommended
- texlive-lang-portuguese
- graphviz

## Serviços Externos

- [Let's Encrypt](https://letsencrypt.org)

## Variáveis de Ambiente

As variáveis abaixo são comuns entre os ambientes.
A variável **DJANGO_CONFIGURATION** carrega as configurações de cada ambiente.
Os valores possíveis são: Development, Staging, Production.

**Development:** Define o ambiente como development (desenvolvimento),
neste modo as funções de **DEBUG** estão ativadas.

**Staging:** Define o ambiente como staging (pré produção),
neste modo as funções de **DEBUG** ficam desativadas e o compartilhamento
de recursos de origens cruzadas (CORS) ficam restritas ao localhost.
Também variáveis de segurança são ativadas para proteção da aplicação.

**Production:** Define o ambiente como production (produção),
neste modo as configurações do ambiente staging são herdadas
e o serviço de **memcache** ativado.

.. code-block:: python

    PROJECT=backend
    DEBUG=True
    DJANGO_SETTINGS_MODULE=backend.settings
    DJANGO_CONFIGURATION='Development'
    SECRET_KEY='x_849%m7$$z1&b90ws3ey%&n*sgs6ˆs3$9_3g^ymi4164y1ppv-dm'
    FIELD_ENCRYPTION_KEY='f164ec6bd6fbc4aef5647abc15199da0f9badcc1d2127bde2087ae0d794a9a0b'
    DATABASE_URL=postgres://postgres:postgres@127.0.0.1:5432/backend_test

## Como executar a aplicação localmente (Linux)

A execução abaixo presume que em seu ambiente de desenvolvimento exista as soluções do docker e docker-compose instalados e configurados de forma adequada.

Caso tenha dúvidas de como preparar o ambiente acompanhe a documentação em: [Docker Documentation](https://docs.docker.com/)

Executando:

.. code-block:: shell

    cp docker-compose-sample.yml docker-compose.yml
    docker-compose up

Basta acessar o endereço no seu navegador: <http://localhost:8000/admin>

- Login: admin
- Senha: DesafioHyperativa

## Utilizando a API

### Requisitando o token JWT

```sh
curl -d '{"username": "admin","password": "DesafioHyperativa"}' \
     -H "Content-Type: application/json" \
     -X POST http://127.0.0.1:8000/api/token/
```

### Resultado esperado:

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMjg1MDQzNCwianRpIjoiMTg2MWQ4ZDZkMDVlNDhmMDkwMmI5OWNiZmM1MzU5NDAiLCJ1c2VyX2lkIjoxfQ.Z3lmckvTGh-RqEbQffAA17BTN9OT3CcR6HNaEs2Fzvk",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIyODUwNDM0LCJqdGkiOiIyNDhhZTc0ZTc4Yzk0MTJhOTk3MjcwYTRlNmQwYmIyMyIsInVzZXJfaWQiOjF9.fNpOZuCROeQ94hHoLjdvNH0hI7y8WccUM0Amo-NPGE0"
}
```

### Upload do arquivo TXT

```sh
+ curl -F post=@contrib/DESAFIO-HYPERATIVA.txt -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIyODUwNDM0LCJqdGkiOiIyNDhhZTc0ZTc4Yzk0MTJhOTk3MjcwYTRlNmQwYmIyMyIsInVzZXJfaWQiOjF9.fNpOZuCROeQ94hHoLjdvNH0hI7y8WccUM0Amo-NPGE0' -X POST http://127.0.0.1:8000/api/app/card/upload
```

### Busca pelo número do cartão:

```sh
curl -X GET "http://localhost:8000/api/app/card/search/456897912999999" \
	-H  "accept: application/json" \
	-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIyODUwNDM0LCJqdGkiOiIyNDhhZTc0ZTc4Yzk0MTJhOTk3MjcwYTRlNmQwYmIyMyIsInVzZXJfaWQiOjF9.fNpOZuCROeQ94hHoLjdvNH0hI7y8WccUM0Amo-NPGE0"
```

#### Resultado esperado:

```json
[
  {
    "id": "394deedb-af6f-4236-9115-5c022e67f651",
    "tag": "C",
    "batch": "10    ",
    "number": "456897919999999"
  },
  {
    "id": "09ed26e3-fa2c-4b05-bfeb-03b153a70f1a",
    "tag": "C",
    "batch": "9     ",
    "number": "456897999099999"
  },
  {
    "id": "2a673631-714f-4a5b-a3b8-110e8e0ac08b",
    "tag": "C",
    "batch": "8     ",
    "number": "456897919999999"
  },
  {
    "id": "897bcefe-88b0-41ad-81e3-7b3d5af12e0e",
    "tag": "C",
    "batch": "7     ",
    "number": "45689799999998"
  },
  {
    "id": "b69c1e96-a31b-4b5c-a0ab-ebd1e89a0d13",
    "tag": "C",
    "batch": "6     ",
    "number": "456897912999999"
  },
  {
    "id": "3d3cbf1e-380f-49ee-a2cc-3077eaf752e8",
    "tag": "C",
    "batch": "5     ",
    "number": "456897999999999124"
  },
  {
    "id": "7f2df159-df20-47b3-91f7-4a21d724b6a6",
    "tag": "C",
    "batch": "4     ",
    "number": "456897998199999"
  },
  {
    "id": "87c158a5-c3e1-43f2-9d31-94c5edb20e6d",
    "tag": "C",
    "batch": "3     ",
    "number": "456897999999999"
  },
  {
    "id": "570f4f84-43dc-4da4-81e2-7d2666292538",
    "tag": "C",
    "batch": "1     ",
    "number": "456897922969999"
  },
  {
    "id": "7ab5e50c-876d-4515-b945-d711e38378b3",
    "tag": "C",
    "batch": "2     ",
    "number": "456897999999999"
  },
  {
    "id": "bce690af-014d-46f2-8604-d858e290c593",
    "tag": "C",
    "batch": "10    ",
    "number": "456897919999999"
  },
  {
    "id": "d884e0db-f0a8-4889-860c-04f38b0c47a0",
    "tag": "C",
    "batch": "9     ",
    "number": "456897999099999"
  },
  {
    "id": "56d006b8-9150-492b-8505-7b7b46996002",
    "tag": "C",
    "batch": "8     ",
    "number": "456897919999999"
  },
  {
    "id": "017356a9-453d-4986-80db-3fc606ebe79b",
    "tag": "C",
    "batch": "7     ",
    "number": "45689799999998"
  },
  {
    "id": "76a1a833-4e5a-4021-8c23-860e9c7485d2",
    "tag": "C",
    "batch": "6     ",
    "number": "456897912999999"
  },
  {
    "id": "7cd963c2-c9c7-45ae-af45-6abf1be8bf5e",
    "tag": "C",
    "batch": "5     ",
    "number": "456897999999999124"
  },
  {
    "id": "4926afb8-ae99-4f10-81e0-87b598cb2c22",
    "tag": "C",
    "batch": "4     ",
    "number": "456897998199999"
  },
  {
    "id": "aa51acd2-9ba4-4697-8ac5-6711cd770db3",
    "tag": "C",
    "batch": "3     ",
    "number": "456897999999999"
  },
  {
    "id": "43b0652e-c926-4f30-99e6-e9c98dd76d4a",
    "tag": "C",
    "batch": "1     ",
    "number": "456897922969999"
  },
  {
    "id": "0dc07509-74ff-4390-9918-b9737b553755",
    "tag": "C",
    "batch": "2     ",
    "number": "456897999999999"
  }
]
```

### Evidências da criptografia sens[iveis no banco de dados

``````
--
-- Data for Name: app_card; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_card (id, created_at, updated_at, name, date, batch, qty_records) FROM stdin;
3ffb5873-29d0-4f01-aa4a-eeb5191e9ecf    2021-05-05 23:43:53.918+00      2021-05-05 23:43:53.918+00      \\xdb880dfc16aa90749eb47127e5c588ec7fce96aaf887e3a0def06eac43b1e567c583525dc16583ea99ca595e1acb4622bf553e1753fcbf76c12d0fdc73  \\xf490c24402c0aa7e09f493fe3dc619a2d160a657dd61dcd16783d19f3952b3d2891bbde87650cd16     \\x9e9adcd11bb969fe0e536cf187935ace46cc94ed718ea3996832702e4deaed31777ef9a83fe82584     \\xa400d49e21adab5dc90f3fd4cb77c54dcf8110327a2a6e278417e262068fed70e922a9a00e9c
633c8910-8e22-4e1c-884d-72f4aa843f96    2021-05-05 23:43:43.859+00      2021-05-05 23:43:43.859+00      \\x0f85054f86de62fd243bf1b5aa7ba6a88e477fc92a708a8b8ae5e684ea3e176a53f3771220be986b293af7aeb2fd7aebe3241f3e000f777b057ee006d2  \\x72766ce69a95ac04c4e894629cc2137af4d90be87896eba4554c1731e3edeb210b980f5c1d878ede     \\xbb1da516038100e251a45d9eafaf1217b1d98abd6499f6d26fc1c3059984e1bb86c05f3d32440752     \\xc2b8ea0d520c47afb000c41ee9d544f6b147fcfb895a3821e6fa3d759120acffec5107770c1d
93ff0965-2f65-4a87-a74e-d3005781ac28    2021-05-05 23:24:52.404+00      2021-05-05 23:24:52.404+00      \\x0d98bf515cb75b3c6e5e3a56355ffd127e932d5e2286010a1bddfe3dc8fe8b7e59062e4c4c58ffdb3e0d9b545088eb4e2021a155a2a4d8adfec3b369d4  \\x42486919bae38c98de8049f99e56488c62f7b59697db6964d68716e442d9b1092d539caf6749acff     \\x78dba863e8cad01b98153c9eef74e95010f77f8e92c1fe6f66719eba4098a93ec3d29306811e86f5     \\x2571fbc26647c2feb16f70a32e577021630c53a6bd46762a4a82a72ad0476b1d429310337fc8
b1550b1f-84cc-4816-99cb-296e97f4d1af    2021-05-05 23:05:07.803+00      2021-05-05 23:05:07.803+00      \\xdc69578869dff7d0864b18965b7aeeba35798b5831cbf37d29032f26487da53a0a90fd0a98c1870b3c7e756e2e5ecd4d1a34dcdcb2e3aa14e235ba1aec  \\xc79d024c169e6c57ff1f826b7ff90acc040d0cc0a4bb6fb02b23b134395bfd3f8cc43d553e4e20f8     \\x7474ea6a2a6cf4c6dca620e929f4994c85cbb9645e3793ae2298613f1a93067a54f1ca5a0b7b700d     \\x600fb7982bba879febade28f6f1edacc0c49c557ae40cb50b5c36c2f6d239247ee5cb9ad4669
c2b4fe7d-e9ce-4ada-9efa-bcc4e40ac061    2021-05-05 23:49:06.954+00      2021-05-05 23:49:06.954+00      \\xb365ed1689c9e89ab8f6abec4ad9871cdf6b8380a5b0b1b37dd05078ab1ff774bc6497dd5293d3107fac75b1781781cf2a026df02d19b47daa504b7a4f  \\x09a4441e7ea0040729fab66e4bb381012cc659c70f2f751bc0afbc6668f6ce41d89320b1b6d4ce34     \\xc0165af3136ea0e0d7eef04b0104b033ff033ab107bbbec8f1eb9ea7cbb17043ec02cdb1b96c6973     \\x6c4963ce5f0a500fd6fcb67830552be2f249f86c44fc565a727358020960df3a0b05f692452e
\.
`````
``````
