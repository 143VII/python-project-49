
brain-game:
	poetry run brain-game

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-primes:
	poetry run brain-prime
	
brain-progression:
	poetry run brain-progression

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games