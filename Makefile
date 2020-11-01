default:
	@g++ -Wall T.cpp -o Out
	./Out
	@rm Out

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
	
reset:
	@tput bold;
	@tput setaf 6; 
	@printf "DIR NAME > "
	@tput sgr0
	@read NAMEDIR; \
	cp -r INROUND/ $$NAMEDIR/
	@rm -f INROUND/*.cpp
	@rm -f INROUND/a
	@rm -f INROUND/b
	@rm -f INROUND/c
	@rm -f INROUND/d
	@rm -f INROUND/e
	@rm -f INROUND/f
	@tput sgr0
	@echo ""

stress:
	@cat inputf.in > saveIn.txt
	g++ -Wall T.cpp -o myOut
	g++ -Wall brute.cpp -o bruteOut
	python3 stressCheck.py
	@cat saveIn.txt > inputf.in
	@rm ./myOut ./bruteOut saveIn.txt
	
