import os
from dotenv import load_dotenv
from src.process_grp import create_app


load_dotenv()


def main():

    app = create_app()

    is_local = os.environ.get('ENV') == 'local'
    if is_local:
        app.run(
            debug=True,
            host='0.0.0.0',
            port=int(os.environ.get('BACKEND_PORT', 5000))
        )
    else:
        app.run()


if __name__ == '__main__':
    main()
