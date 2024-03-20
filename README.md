# deltimesh
deltimesh - утилита для ALT Linux Regular для удаления автоматических снапшотов Timeshift, помеченных как "Before Offline Update".

## Установка
Для установки нам потребуется *git*. Установим его.
```bash
su -c "apt-get install git"
```

Далее подготавливаем папку и скачиваем скрипт.
```bash
mkdir ~/.catcatcher && cd ~/.catcatcher && git clone https://github.com/ImCatCatcher/deltimesh.git
```

Устанавливаем его.
```bash
su -c "ln -s $HOME/.catcatcher/deltimesh/deltimesh.py /usr/bin/deltimesh && chmod +x /usr/bin/deltimesh"
```

## Использование

### Вручную
Скрипт можно использовать вручную, для этого нам потребуются права root.
```bash
su -c "deltimesh"
```

### Автоматически
Также возможно использование скрипта на автозагрузке как сервиса для systemd.

Установим его.
```bash
su -c "cp $HOME/.catcatcher/deltimesh/deltimesh.service /etc/systemd/system/deltimesh.service"
```

Теперь включим.

```bash
su -c "systemctl enable deltimesh"
```
