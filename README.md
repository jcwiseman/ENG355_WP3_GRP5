# ENG355_WP3_GRP5

A math library, but for animals.

## Run

    pip install -r requirements.txt
    python app.py

- Demo: http://localhost:5000/
- Documentation: http://localhost:5000/docs
- API: http://localhost:5000/api/sqrt?animal=cat

## Where things go

- `api.py`: write API functions here. Each public function automatically gets
  an `/api/<name>` URL and shows up on the demo page.
- `app.py`: the Flask server. You shouldn't need to change it.
- `templates/index.html`: demo page.
- `static/docs.html`: the documentation. Write it by hand here.
