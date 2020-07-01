# import os
from handlers import a
from flask import Flask

if __name__ == "__main__":
	# port = int(os.getenv('PORT', 5000))
	a.run(debug=True)
		