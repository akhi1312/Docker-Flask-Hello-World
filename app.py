from github import Github ,GithubException,RateLimitExceededException
from github import UnknownObjectException
from sys import argv
from flask import Flask


n = str(argv[1])

# checking valid Github url

if 'github' not in n:
    print "Invalid URl please try again"
    exit()

# Fetching Username and Repsoitory name
n = n.split('/')
username = n[3]
repos = n[4]


app = Flask(__name__)


@app.route("/v1/<file>")
def displayFile(file):
    try:
        if file.lower().endswith(('.yml', '.json', '.yaml')):
        # First create a Github instance:
            g = Github()
            repo = g.get_user(username).get_repo(repos)
            file_content = repo.get_contents(file)
            return file_content.decoded_content

        else:
            return "404 Page Not Found "
    except RateLimitExceededException:
        return "Exception raised when the rate limit is exceeded try after some time "
    except UnknownObjectException:
        return " Exception raised when a non-existing object is requested"
    except GithubException as error:
        return error

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

