SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/exor.v
VERILOG_SOURCES += $(PWD)/../wrappers/exor_test.v

exor:
        $(MAKE) sim MODULE = exor_test TOPLEVEL = exor_test
include $(shell cocotb-config --makefiles)/Makefile.sim
