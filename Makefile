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
	@mkdir temp
	@touch temp/inputf.in
	g++ -Wall sols/main.cpp -o temp/myOut
	g++ -Wall sols/brute.cpp -o temp/bruteOut
	python3 stress-check.py
	@rm -rf temp

clean:
	@rm -rf temp __pycache__
