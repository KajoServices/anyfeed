# anyfeed

Anywhere live feed client.

## Requirements
* Python 3.5+
* Tornado 4.3+

## Setup environment

    $ python3 -m venv anyfeed
    $ source anyfeed/bin/activate
    $ pip install -r requirements.txt

## Usage

Contact us to get the feed address and access key file.

Place access key file (`server.key`) to the application directory.

Change `TLS_HOST` in `settings.py` to obtained ip address.

Go to Terminal and subscribe to feed via web-client:

    $ python client.py --logging=debug

Open a browser, go to [http://localhost:8000/](http://localhost:8000/) and press 'Connect'.

Enjoy!
