# Meetup.com API notes

* [API landing page](https://www.eventbrite.com/platform/api)


## Create your API key

Single users can use an API key, App Partners will need to use OAuth.

We use this key in exploration, tests, etc.

1. Create an account at [https://www.eventbrite.com](https://www.eventbrite.com)
1. or, sign in
1. Browse [https://www.eventbrite.com/platform/api-keys](https://www.eventbrite.com/platform/api-keys)
1. Copy the "URL Example" from this page and paste it into a browser window to prove it works.
1. Add the following to your `.zshrc`, `.bashrc` or similar and source it. Note: If using PyCharm, you will have to restart it to pick up changes.
    ```bash
    export EVENTBRITE_KEY='YOUR API KY GOES HERE'
    ```
1. Restart your shell to reload this config.
1. Verify it loaded properly
    ```bash
    ᐅ source ~/.zshrc
    ᐅ env | sort | grep EVENTBRITE
    EVENTBRITE_KEY=XXXXXXXXXXXXXXXX
    ```
1. or, you can add this env var to your PyCharm project config


## First request



