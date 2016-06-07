## Rozwiązanie problemu dowozu dzieci

### Wprowadzenie
Problem dowozu dzieci zdefiniowany jest następująco: mamy N przystanków, na każdym z nich stoi pewna liczba dzieci. 
Mamy do dyspozycji autobusy, każdy z nich ma ograniczoną pojemność (liczoną w liczbie dzieci). Oprócz tego każdy autobus nie może
jechać dłużej niż zdefiniowany maksymaly dystans. Każdy autobus zaczyna i kończy drogę w szkole.
Celem jest zminimalizowanie liczby autobusów w ten sposób, by wszystkie dzieci zostały dowiezione do szkoły.

### Idea algorytmu
Algorytm w każdym kroku działa w dwóch fazach: fazie przydzielania przystanków i fazie znajdowania optymalnej ścieżki. 
Na samym początku każdy autobus ma przydzielony dokładnie jeden przystanek. Faza przydzielania przystanków polega na znalezieniu
najlepszego autobusu, którego trasę można połączyć z pierwszym nieprzepełnionym autobusem. Autobus jest przepełniony, gdy nie może
odwiedzić już żadnego przystanku ze względu na jedno z ograniczeń wejściowych.

Faza znajdowania optymalnej ścieżki korzysta z algorytmu ACO (ant colony optimization) i służy do wyliczenia najlepszej (względem
długości ścieżki) kolejności odwiedzenia przystanków w nowo połączonym zbiorze.

Algorytm kończy działanie, gdy wszystkie autobusy (być może poza ostatnim) są przepełnione.
