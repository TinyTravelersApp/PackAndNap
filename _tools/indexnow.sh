#!/bin/sh
# Tell IndexNow (Bing, Yandex and others) which pages changed. Run after each deploy.
# Pass page URLs as arguments; with none, every page in the sitemap is sent.
URLS=${*:-"https://packandnap.com/ https://packandnap.com/privacy/ https://packandnap.com/delete-account/"}
LIST=$(printf '"%s",' $URLS | sed 's/,$//')
curl -sS -o /dev/null -w "IndexNow HTTP %{http_code}\n" -X POST https://api.indexnow.org/indexnow \
  -H "Content-Type: application/json; charset=utf-8" \
  -d "{\"host\":\"packandnap.com\",\"key\":\"40d71ac5a7fcfec9e97e5bf19b3f601f\",\"keyLocation\":\"https://packandnap.com/40d71ac5a7fcfec9e97e5bf19b3f601f.txt\",\"urlList\":[$LIST]}"
