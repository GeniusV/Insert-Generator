# Insert-Generator
数据生成器，应付作业专用


## Usage

g = DateGenerator([table-name], [dict with field names and factories], [number to generate])

``` python
    name = NameFactory()
    address = AddressFactory()
    phone_num = PhoneNumFactory()

    dic = {'name': name, 'address': address, 'phone': phone_num}
    g = DateGenerator("tablename", dic, 10000)
    g.run()
 ```
 
All field names and Factories shoud be placed into a dict

Custom field data generator can inhert from `Factory`, which has only one method `get()`.
 
