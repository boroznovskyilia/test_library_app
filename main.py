from services.library_service import LisbraryService
from services.cli_service import CliCervice
from models.repository import LibraryRepository
from models.models import Library

def main():
    cli_service = CliCervice(LisbraryService(LibraryRepository(Library())))
    cli_service.start()

if __name__ == '__main__':
    main()