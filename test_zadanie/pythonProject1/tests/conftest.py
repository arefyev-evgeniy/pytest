import pytest

def pytest_sessionstart(session):
    print("Начало тестовой сессии")

def pytest_sessionfinish(session, exitstatus):
    print("Конец тестовой сессии")

def pytest_addoption(parser):
    parser.addoption("--logs", action="store", default="False", help="Enable or disable logging (True/False)")