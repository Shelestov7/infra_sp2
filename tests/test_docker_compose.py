import os
import re

from django.conf import settings


class TestDockerfile:

    def test_dockerfile(self):
        try:
            with open(f'{os.path.join(settings.BASE_DIR, "docker_compose.yaml")}', 'r') as f:
                docker_compose = f.read()
        except FileNotFoundError:
            assert False, 'Проверьте, что добавили файл docker_compose.yaml'

        assert re.search(r'image:\s+postgres:latest', docker_compose), \
            'Проверьте, что добавили образ postgres:latest в файл docker_compose'
        assert re.search(r'build:\s+\.', docker_compose), \
            'Проверьте, что добавили сборку контейнера из Dockerfile в файл docker_compose'
