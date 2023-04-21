# В данной конфигурации мы предполагаем, что мы получаем изображение непосредственно из базы данных
# На практике может быть такое, что мы будем получать только ссылку на изображение, тогда потребуется другая логика
from sqlalchemy import Column, Integer, VARCHAR, BLOB

from .base import BaseModel


class AnimalsPictures(BaseModel):
    __tablename__ = 'animals_pictures'
    image_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    title = Column(VARCHAR(50), nullable=False)
    # сюда записываем url или путь к папке, где лежит картинка, если мы не храним её в базе
    # ссылка может отсутствовать, но должна быть уникальной для каждого файла
    image_link = Column(VARCHAR(150), unique=True, nullable=True)
    # колонка для хранения самого файла изображения, если мы решили записать его непосредственно в базуengine
    image = Column(BLOB, unique=True, nullable=True)
