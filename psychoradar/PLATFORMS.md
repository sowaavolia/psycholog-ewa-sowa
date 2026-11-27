# PsychoRadar CALL — Android i komputer

Dwie wersje instalacyjne, jedna logika publikowania i kontroli budżetu.

## Android
Docelowo aplikacja APK: lokalna biblioteka grafik, kolejka publikacji, powiadomienia, panel kosztów. Harmonogram przez Android WorkManager; zadania w tle mogą się opóźniać.

## Komputer
Docelowo aplikacja instalacyjna Windows (np. Tauri): te same funkcje, lokalna baza, harmonogram uruchamiany podczas pracy komputera. Możliwe późniejsze wsparcie Linux/macOS.

## Wspólny rdzeń
- Projekt posta: zdjęcie, opis, kanały, termin, status zatwierdzenia.
- Bezpieczne przechowywanie danych lokalnych.
- Publikacja przez oficjalne API Meta wyłącznie po uzyskaniu właściwych uprawnień.
- Historia prób, błędów i potwierdzonych publikacji.
- Reguły budżetowe: alert i wstrzymanie tylko gdy dostępne są odpowiednie uprawnienia API.

## Granice
Nie używać tokenów Upload-Post jako tokenów Meta. Nie obiecywać publikacji w prywatnych grupach. Nie przechowywać sekretów aplikacji Meta w kodzie klienta. Jeśli API wymaga poufnego sekretu lub publicznego callbacku, potrzebny będzie bezpieczny pośrednik. Żadna wersja nie jest jeszcze zbudowana ani zainstalowana.

## Kolejność
1. Wspólny model danych i lokalny harmonogram.
2. Ekran kolejki i testy bez prawdziwego publikowania.
3. Bezpieczne logowanie Meta i testowa publikacja na stronie gabinetu.
4. APK Android i instalator Windows, testy na urządzeniach.
