import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from apps.api.adapters import orm
from apps.api.domain import model


def init_mock_data(session):
    session.query(model.Book).delete()
    session.query(model.Tag).delete()


@pytest.fixture
def client():
    from apps.entrypoint import app

    app_context = app.app_context()
    app_context.push()
    client = app.test_client()
    yield client
    # Teardown
    app_context.pop()


@pytest.fixture
def in_memory_sqlite_db():
    engine = create_engine('sqlite:///:memory:')
    orm.metadata.drop_all(engine)
    orm.metadata.create_all(engine)
    yield engine
    orm.metadata.drop_all(engine)


@pytest.fixture
def sqlite_session_factory(in_memory_sqlite_db):
    yield sessionmaker(bind=in_memory_sqlite_db)