from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()

table_registry.mapped_as_dataclass


class YourModelName:
    __tablename__ = 'your_table_name'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)

    # column_name: Mapped[datatype] = mapped_column()
