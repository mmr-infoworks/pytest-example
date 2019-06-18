import pytest
@pytest.fixture(scope="session")

def some_resource(request):
  print('\nSome recource')

  def some_resource_fin():
    print('\nSome resource fin')

  request.addfinalizer(some_resource_fin)