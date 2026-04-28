from importlib.util import spec_from_file_location, module_from_spec
from json import load
from json.decoder import JSONDecodeError
from os.path import basename, splitext
from pathlib import Path
from sys import argv, exit
from typing import Callable

# 고정 정보.
QUIZ_PATH = "./path.json"
CODE_NAME, EXAMPLE_NAME = "code.py", "examples.json"
TARGET_FCT = "solution"


# 경로 path의 JSON 형식 딕셔너리를 반환합니다.
def load_json(path: Path) -> dict:
  try:
    with open(path, 'r') as f:
      return load(f)
  except FileNotFoundError:
    print(f"driver: [{path}] 파일이 존재하지 않습니다.")
    return {}
  except JSONDecodeError:
    print(f"driver: [{path}] 파일의 JSON을 불러올 수 없습니다.")
    return {}

# 경로 path의 name 이름을 가진 함수를 반환합니다.
def load_function(path: Path, name: str) -> Callable:
  try:
    module_name = splitext(basename(path))[0]
    spec = spec_from_file_location(module_name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, TARGET_FCT)
  except FileNotFoundError:
    print(f"driver: [{path}] 파일이 존재하지 않습니다.")
    return None
  except AttributeError:
    print(f"driver: [{path}] 파일의 {name} 함수가 존재하지 않습니다.")
    return None

# 함수 fct를 args 매개 변수로 실행합니다.
def run(fct: Callable, args: list) -> list:
  try:
    return [fct(*args)]
  except Exception:
    print(f"driver: 코드를 실행할 수 없습니다.")
    return []


def main():
  # 입력 받은 인자 설정.
  try:
    location, id = argv[1], argv[2]
  except IndexError:
    print("driver:", "인자를 찾을 수 없습니다.", "프로그램을 실행하려면 다음 명령을 입력하세요.")
    print("\t", "python3 driver.py <문제 출처> <문제 번호>")
    print("\t", "문제 출처: [PCCE]")
    exit(0)

  quiz_path = Path(load_json(QUIZ_PATH).get(location, "").get(id, ""))
  examples_path = quiz_path/EXAMPLE_NAME
  code_path = quiz_path/CODE_NAME

  # 예제, 함수 불러오기.
  examples = load_json(examples_path)
  solution = load_function(code_path, TARGET_FCT)

  id = 0
  for example in examples:
    # 입출력, 인자 설정.
    id += 1
    args, expects = example['inp'], example['out']

    # 테스트 수행.
    tests = run(solution, args)

    # 실행 결과 출력.
    result = (expects == tests)
    print('=====', 'example', id, '=====')
    print('input:', args)
    print('expected output:', expects)
    print('test output:', tests)
    print('test result:', 'success' if result else 'failure')
    print()


if __name__ == "__main__":
  main()