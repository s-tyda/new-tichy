## Konfiguracja CLion
- Upewniamy się, że mamy zainstalowaną wtyczkę **Python Community Edition**. W tym celu otwieramy **File->Settings->Plugins->Installed** (ctrl+alt+S) i wyszukujemy **Python Community Edition**.

![img_06](../images/img_06.png?raw=true)

- Następnie przechodzimy do zakładki **Build, Execution, Deployment->Python Interpreter**, w rozwijanej liście wybieramy **Show all**, a nastęnie klikamy **add**.

![img_07](../images/img_07.png?raw=true)

- W menu po lewej wybieramy **System Interpreter** i w rozwijanej liście wybieramy naszą minicondę. Jeśli jej nie ma to trzeba ją dodać ręcznie. W tym celu trzeba nacisnąć **trzy kropki** (shift+enter) i wskazać ścieżkę do pliku **python.exe** w folderze z condą (domyślnie jest to **C:\Users\user\miniconda3\python.exe**).

![img_08](../images/img_08.png?raw=true)

- Wybieramy nowo dodany interpretator i zatwierdzamy podwójnie **OK**. Po zatwierdzeniu odczekujemy chwilę aż środowisko załaduje interpretator.
- Następnie wystarczy już tylko dodać konfigurację uruchamiania. Na głównym pasku wybieramy **Run->Edit Configurations**. Plusikiem dodajemy nową konfigurację, wybierając jako szablon **Python**. W polu **Script path** wybieramy ścieżkę do skryptu. W polu **Parameters** ustawiamy kolejno parametry: **nr_zadania** (np. 4) **$FilePath$**. Na koniec w polu **Python interpreter** zaznaczamy **Use specified interpreter** i wybieramy naszą minicondę.

![img_09](../images/img_09.png?raw=true)