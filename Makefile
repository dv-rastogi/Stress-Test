run:
	@tput bold;
	@tput setaf 6; 
	@printf "C++ FILE NAME > "
	@tput sgr0
	@read NAME; \
	g++ $$NAME.cpp -o Out  
	./Out
	@tput sgr0
	@rm Out
	@echo ""

stress: clean 
	@mkdir _temp
	@touch _temp/inputf.in 
	g++ -Wall sols/main.cpp -o _temp/myOut
	g++ -Wall sols/brute.cpp -o _temp/bruteOut
	python3 stress-check.py
	@rm -rf _temp __pycache__

clean:
	@rm -rf _temp __pycache__