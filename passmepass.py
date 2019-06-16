import sys
import optparse
import time
from core.main import shell
from core.printf import printf
#try:
#    from lib.bs4 import BeautifulSoup as bs
    #from library.bs4 import BeautifulSoup4 as bs
#except ImportError:
#    printf(1, "Please install beautifulsoup 4 to continue ...")

    

def py_version():
    if sys.version_info.major == 2:
        pass
    elif sys.version_info.major == 3:
        printf(1,"passmepass has no support for python3.")
    else:
        printf(1,"your python version is very old........")
        

def platform():
    import sys
    if sys.platform.startswith('linux'):
        printf(2,"Running passmepass on linux ... (All good)")
    elif sys.platform.startswith('darwin'):
        printf(2,"Running passmepass on \'Mac\' (Not tested)")        
    elif sys.platform.startswith('win32'):
        printf(2,"Running passmepass on \'Windows\' (Not tested)")
    else:
        printf(2,"If \'passmepass\' runs sucsessfuly on your platform %s\nPlease contact me twitter! @1ibr4" %sys.platform)




def main():
    py_version()
    platform()
    parser = optparse.OptionParser()
    parser.add_option("-q", "--quiet", dest="quiet_mode_opt", action="store_true", default=False, help="Runs without displaying the banner.")
    parser.add_option("-p", "--profile", dest="profile", help="|_O4d passmepass profile.")
    options,r = parser.parse_args()

    if options.profile:
        from core.main import shell_noint
        shell_noint(options.profile)
    else:
        from core.main import shell
        shell()

if __name__ == '__main__':
    main()
