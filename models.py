from sqlalchemy import declare_base
from sqlalchemy.orm import Mapped, mapped_column


Base = declare_base()


class ItemModel(Base):
	__tablename__ = 'items'
	
	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str] = mapped_column()

	def __str__(self):
		return self.title


a1 = ItemModel(title='asd')
print(a1)
