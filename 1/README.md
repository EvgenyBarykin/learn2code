# Lesson 1

## GITHUB

- зарегались на github.com
- создали репозиторий
- создали ключ ssh

```bash
ssh -keygen -t ed25519 -C "@mail"
```
- сохранили ключи
- закинули публичный ключ на GitHub (https://github.com/settings/keys)

установили инструменты разработчика 
```bash
xcode-select --install
```

- клонировали репозиторий на комп

```bash
git clone https://github.com/settings/keys
```
- открыли его в Visual Code
- Поставили HomeBrew (для установки разных вещей на Мac) - пакетный менеджер

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
- и установили питон
```bash
brew install python
```