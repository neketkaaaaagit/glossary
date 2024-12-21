from main import SessionLocal, GlossaryTerm

# Глоссарий
glossary = [
    {"name": "Трекинг взгляда (Eye Tracking)", "description": "Технология, предназначенная для измерения движений глаз и направления взгляда, которая используется в различных областях, таких как психология, медицина, маркетинг и интерфейсы человек-компьютер."},
    {"name": "PyGaze", "description": "Открытая библиотека для анализа движений глаз и трекинга взгляда, поддерживающая интеграцию с различными устройствами, такими как Tobii и EyeLink."},
    {"name": "MediaPipe", "description": "Фреймворк от Google, предоставляющий инструменты для анализа изображений и видео, включая детекцию лица, отслеживание жестов и движений глаз."},
    {"name": "dlib", "description": "Популярная библиотека машинного обучения и компьютерного зрения, включающая инструменты для детекции лиц, анализа выражений и трекинга взгляда."},
    {"name": "iTracker", "description": "Система, основанная на машинном обучении, для трекинга взгляда с использованием камер, встроенных в мобильные устройства или ноутбуки."},
    {"name": "SalGAN", "description": "Генеративно-состязательная сеть (GAN), используемая для предсказания карт внимания (saliency maps), отображающих области, привлекающие наибольшее внимание зрителя."},
    {"name": "Карта внимания (Saliency Map)", "description": "Визуализация, показывающая наиболее значимые области изображения, на которые обычно обращает внимание человек."},
    {"name": "Генеративно-состязательные сети (GAN, Generative Adversarial Networks)", "description": "Класс алгоритмов машинного обучения, состоящих из двух сетей: генератора, создающего данные, и дискриминатора, отличающего сгенерированные данные от реальных."},
    {"name": "Рентгенология (Radiology)", "description": "Область медицины, занимающаяся использованием рентгеновских лучей, ультразвука и других методов визуализации для диагностики и лечения заболеваний."},
    {"name": "Мониторинг работы рентгенолога", "description": "Процесс наблюдения и анализа действий рентгенолога при интерпретации медицинских изображений с целью повышения точности диагностики и уменьшения ошибок."},
    {"name": "Аппаратный трекинг взгляда (Hardware Eye Tracking)", "description": "Технология, использующая специализированные устройства, такие как очки или камеры, для отслеживания движений глаз. Примеры устройств: Tobii, EyeLink."},
    {"name": "Визуальная нагрузка (Visual Load)", "description": "Количество и сложность визуальной информации, обрабатываемой человеком в процессе выполнения задачи."},
    {"name": "Оценка производительности (Performance Assessment)", "description": "Процесс измерения точности и скорости выполнения задач, например, рентгенологом, с использованием систем трекинга взгляда."},
    {"name": "Кроссплатформенность (Cross-Platform)", "description": "Способность технологии работать на разных устройствах и операционных системах, например, PyGaze может интегрироваться с Windows, macOS и Linux."},
    {"name": "Машинное обучение (Machine Learning)", "description": "Метод анализа данных и автоматизации, используемый для создания моделей, способных предсказывать или принимать решения, основанные на данных."},
    {"name": "Устройство Tobii", "description": "Один из самых популярных коммерческих трекеров взгляда, предоставляющий точные данные о движениях глаз для исследований и приложений."},
    {"name": "Heatmap", "description": "Тепловая карта, визуализирующая интенсивность внимания на различных участках изображения или экрана."}
]

# Загрузка данных в БД
db = SessionLocal()
for item in glossary:
    term = GlossaryTerm(name=item["name"], description=item["description"])
    db.add(term)

db.commit()
db.close()

print("Глоссарий успешно заполнен.")