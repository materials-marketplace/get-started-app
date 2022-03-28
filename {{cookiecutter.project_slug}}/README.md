# {{ cookiecutter.app_name }}
{{ cookiecutter.app_short_description}}

## 0. Prerequisites

### Deployment target
One should develop and test the application directly on a development machine.
However, once the app is to be registered with MarketPlace it is better to have a more permanent, publicly available URL from which the application can be reached.

For testing, or in case you do not have your own https (sub)domain available, you can use [heroku](https://heroku.com).
To use heroku:
1. Create an account on https://heroku.com
1. Install the [heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
1. Create the app, by executing
```sh
heroku login -i
heroku container:login
heroku create --region=eu {{ cookiecutter.project_slug }}
```

## 1. Register the app

Here you will need the  `openAPI.yml` file generated during the application creation.

For a detailed explanation on the app registration process, please refer to the [MarketPlace documentation](https://materials-marketplace.readthedocs.io/en/latest/).

Please store temporarily the `client_id` and `client_secret` values for the next step.

## 2. Build the app
The app is now ready to be built and deployed.
Make sure that any required port-forwarding is set up so that your app is accessible from the outside.

Next, you need to define your own values via environment values.
For that, we have created a file called `.env` in the project root.
Update it to include the `client_id` and `client_secret` generated by the MarketPlace
```sh
export CLIENT_ID="<client_id_from_registration>"
export CLIENT_SECRET="<client_secret_from_registration>"
```
## 3. Deploy the app

Now the environment values can be made available to the app by running
```sh
source .env
./prepare_deployment.yml
```

### Heroku deployment steps
If you use heroku (and have the appropriate libraries installed), you can deploy by running:
```sh
./deploy_heroku.sh
```
### Docker deployment steps
If you set up your app using the Docker compose, you can start it via:
```sh
docker-compose up -d
```

Otherwise, follow the instructions of your deployment method of choice.

Note that the code inside `app.py` has been created to be compatible with the secrets approach from docker compose, so other deployment methods might require some tuning of the code.