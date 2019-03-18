all: badge_generator

badge_generator:
	python badge_generator_script.py

clean:
	rm badge_generator_script.py
