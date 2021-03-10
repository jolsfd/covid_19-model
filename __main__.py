import fire
import src.data_import
import src.model

# Mainloop
if __name__ == '__main__':
    # Cli
    fire.Fire({
        'update': src.data_import.update,
        'run': src.model.compare_countrys,
        'countrys': src.model.list_countrys
        })