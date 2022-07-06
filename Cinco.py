from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *

globals()['entorno'] = 'VALOR_INICIAL'

spark = SparkSession.builder.appName('PRUEBA_PYSPARK').getOrCreate()
context = spark.sparkContext
context.setCheckpointDir('/Users/andresbeltran/Documents/SALIDAS_PYSAPRK')

logger = context._jvm.org.apache.log4j
logger.LogManager.getLogger("org").setLevel(logger.Level.ERROR)

parallelism = 64

spark.conf.set('spark.sql.shuffle.partitions', parallelism)
spark.conf.set('spark.default.parallelism', parallelism)

work = {}

work['base'] = (
    spark.read.csv('/Users/andresbeltran/Documents/TEST_CSV/test.csv', header=True, inferSchema=True, sep=';')
).checkpoint()

work['base'].createOrReplaceTempView('base')
work['columna_uno'] = spark.sql('SELECT sum(uno) as uno FROM base')
work['columna_dos'] = spark.sql('SELECT sum(dos) as dos FROM base')
work['columna_tres'] = spark.sql('SELECT sum(tres) as tres FROM base')
work['suma_tres'] = spark.sql('SELECT sum(uno) + sum(dos) + sum(tres) as total FROM base')
work['otra_suma'] = spark.sql('SELECT uno FROM base WHERE uno > 67108864').createOrReplaceTempView('otra_suma')
work['final'] = spark.sql('SELECT uno suma FROM otra_suma')

print('Ejecutando Cuatro.py...')
exec(open('Cuatro.py').read())