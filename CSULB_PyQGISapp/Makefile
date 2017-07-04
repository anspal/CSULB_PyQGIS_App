RESOURCE_FILES = resources.py
default: compile
compile: $(RESOURCE_FILES)
%.py : %.qrc
pyrcc4 -o $@ $<
%.py : %.ui
pyuic4 -o $@ $<
clean:
rm $(RESOURCE_FILES)
rm *.pyc