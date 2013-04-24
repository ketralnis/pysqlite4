#####################################################################
# Makefile originally written by Hans Oesterholt-Dijkema
# Adapted and sanitized by Gerhard Haering for use with the pysqlite
# project.
#
# It works with the free MSVC2003 toolkit as well as with MS Visual
# Studio 2003.
#
# Makefile for SQLITE for use with GNU Make (MinGW/MSYS) 
# and the MSVC2003 free toolkit. Expects the MSVC Free SDK
# installed along with the MSVC2003 free toolkit.
#  
# Expects $INCLUDE, $LIB, $PATH set right for use with CL.EXE in
# MSYS. NEEDS MSYS for clean: and install:, for making only: 
# Works also in the Visual C++ Toolkit 2003 Command Prompt,
# provided %INCLUDE%, %LIB%, %PATH% are set accordingly.
#####################################################################

CL=cl
CLFLAGS=-O2 -Og -G7
LINK=link
PREFIX=$$VCTOOLKITINSTALLDIR
INCINST=$(PREFIX)/include
LIBINST=$(PREFIX)/lib
BININST=$(PREFIX)/bin

SQLITE4_OBJ = alter.o analyze.o attach.o auth.o btree.o build.o \
         callback.o complete.o date.o \
         delete.o expr.o func.o hash.o insert.o \
         main.o opcodes.o os.o os_unix.o os_win.o \
         pager.o parse.o pragma.o prepare.o printf.o random.o \
         select.o table.o tokenize.o trigger.o update.o \
         util.o vacuum.o \
         vdbe.o vdbeapi.o vdbeaux.o vdbefifo.o vdbemem.o \
         where.o utf.o legacy.o loadext.o vtab.o


SQLITE4_OBJ = alter.o analyze.o attach.o auth.o btmutex.o btree.o build.o callback.o \
        complete.o date.o delete.o expr.o func.o hash.o insert.o journal.o \
        legacy.o loadext.o main.o malloc.o mem1.o mem2.o mem3.o mutex.o \
        mutex_w32.o opcodes.o os.o os_win.o pager.o parse.o pragma.o prepare.o \
        printf.o random.o select.o table.o tokenize.o trigger.o update.o utf.o \
        util.o vacuum.o vdbeapi.o vdbeaux.o vdbeblob.o vdbe.o vdbefifo.o vdbemem.o \
        vtab.o where.o

SQLITE4_PRG_OBJ=shell.o 

all: sqlite4.lib
	@echo "done"
 
clean:
	rm -f *.dll *.lib *.exp *.exe *.o

sqlite4.exe: sqlite4.dll $(SQLITE4_PRG_OBJ)
	$(LINK) -OUT:sqlite4.exe $(SQLITE4_PRG_OBJ) sqlite4.lib

sqlite4static.lib: $(SQLITE4_OBJ)
	$(LINK) -LIB -OUT:sqlite4static.lib $(SQLITE4_OBJ)

sqlite4.dll: $(SQLITE4_OBJ)
	$(LINK) -OUT:sqlite4.dll -dll -def:sqlite4.def $(SQLITE4_OBJ)

%.o:	%.c
	$(CL) -c $(CLFLAGS) -Fo$@ $<
