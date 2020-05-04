# Generated by Django 3.0.4 on 2020-04-23 15:21

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200422_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'ABAP'), ('2', 'ActiveMQ'), ('3', 'Ada\xa0programming'), ('4', 'Amazon\xa0Web\xa0Services'), ('5', 'Android'), ('6', 'Angular\xa02+'), ('7', 'AngularJS'), ('8', 'Ansible'), ('9', 'Apache\xa0Hive'), ('10', 'Apache\xa0Kafka'), ('11', 'Apache\xa0Pig'), ('12', 'Apache\xa0Spark'), ('13', 'ARM'), ('14', 'ASP.NET'), ('15', 'ASP.NET\xa0MVC'), ('16', 'Azure'), ('17', 'Backbone.js'), ('18', 'Bash'), ('19', 'Blockchain'), ('20', 'C'), ('21', 'C#'), ('22', 'C++'), ('23', 'CakePHP'), ('24', 'Cassandra'), ('25', 'Chef'), ('26', 'Cisco'), ('27', 'Clojure'), ('28', 'CoffeeScript'), ('29', 'Cordova'), ('30', 'Cross\xa0Platform\xa0Mobile'), ('31', 'Django'), ('32', 'Docker'), ('33', 'Drools'), ('34', 'Drupal'), ('35', 'Elasticsearch'), ('36', 'Elixir'), ('37', 'ELM'), ('38', 'Embedded\xa0Linux'), ('39', 'Ember.js'), ('40', 'Erlang'), ('41', 'ETL'), ('42', 'Ez\xa0Platform'), ('43', 'F#'), ('44', 'Flash'), ('45', 'Flask'), ('46', 'Flutter'), ('47', 'Fortinet'), ('48', 'Fortran'), ('49', 'FPGA'), ('50', 'Go'), ('51', 'Google\xa0Cloud\xa0Platform'), ('52', 'Google\xa0Data\xa0Studio'), ('53', 'Grails'), ('54', 'Grape'), ('55', 'Groovy'), ('56', 'Hadoop'), ('57', 'Haskell'), ('58', 'HBase'), ('59', 'Hibernate'), ('60', 'HTML/CSS'), ('61', 'Hyper-V'), ('62', 'Informatica'), ('63', 'Internet\xa0of\xa0Things'), ('64', 'Ionic'), ('65', 'iOS'), ('66', 'J2EE'), ('67', 'Java'), ('68', 'JavaFX'), ('69', 'JavaScript'), ('70', 'Jenkins'), ('71', 'Joomla'), ('72', 'jQuery'), ('73', 'Juniper'), ('74', 'Keras'), ('75', 'Kotlin'), ('76', 'Kubernetes'), ('77', 'LAN/WAN'), ('78', 'Laravel'), ('79', 'Liferay'), ('80', 'Linux'), ('81', 'Lisp'), ('82', 'Looker'), ('83', 'Magento'), ('84', 'Matlab'), ('85', 'Memcached'), ('86', 'Meteor'), ('87', 'MongoDB'), ('88', 'MySQL'), ('89', '.NET'), ('90', '.NET\xa0Core'), ('91', 'NLP'), ('92', 'Node.js'), ('93', 'Objective-C'), ('94', 'OCaml'), ('95', 'OpenGL'), ('96', 'OpenStack'), ('97', 'Oracle\xa0Database'), ('98', 'Pandas'), ('99', 'Pentaho'), ('100', 'Perl'), ('101', 'PHP'), ('102', 'Pixi.js'), ('103', 'Play'), ('104', 'PL/SQL'), ('105', 'Polymer'), ('106', 'PostgreSQL'), ('107', 'Power\xa0BI'), ('108', 'Prestashop'), ('109', 'Proxmox\xa0Virtual\xa0Environment'), ('110', 'Puppet'), ('111', 'Python'), ('112', 'Pytorch'), ('113', 'Qlik'), ('114', 'Qt'), ('115', 'R'), ('116', 'RabbitMQ'), ('117', 'ReactJS'), ('118', 'React\xa0Native'), ('119', 'Redis'), ('120', 'Redux'), ('121', 'Riot.js'), ('122', 'Ruby'), ('123', 'Ruby\xa0on\xa0Rails'), ('124', 'Rust'), ('125', 'SAS'), ('126', 'SASS'), ('127', 'Scala'), ('128', 'Scheme'), ('129', 'scikit-learn'), ('130', 'Selenium'), ('131', 'SEO'), ('132', 'Shopware'), ('133', 'Sinatra'), ('134', 'Solr'), ('135', 'Spring'), ('136', 'Spring\xa0Boot'), ('137', 'SPSS'), ('138', 'SQL'), ('139', 'SQL\xa0Server'), ('140', 'Stata'), ('141', 'Struts'), ('142', 'Swift'), ('143', 'Symfony'), ('144', 'Tableau'), ('145', 'Talend'), ('146', 'TCL'), ('147', 'TensorFlow'), ('148', 'Terraform'), ('149', 'Tomcat'), ('150', 'T-SQL'), ('151', 'TypeScript'), ('152', 'Unity'), ('153', 'Unix\xa0Shell\xa0Scripting'), ('154', 'VBA'), ('155', 'VB.NET'), ('156', 'Verilog'), ('157', 'VHDL'), ('158', 'VMWare\xa0vSphere'), ('159', 'Vue.js'), ('160', 'VxWorks'), ('161', 'WCF'), ('162', 'Windows'), ('163', 'Windows\xa0Mobile'), ('164', 'WordPress'), ('165', 'WPF'), ('166', 'x86\xa0Assembly'), ('167', 'Xamarin'), ('168', 'Yii'), ('169', 'Zend\xa0Framework'), ('170', 'Microsoft\xa0Office\xa0Word'), ('171', 'Microsoft\xa0Office\xa0Excel'), ('172', 'Microsoft\xa0Office\xa0PowerPoint'), ('173', 'Microsoft\xa0Office\xa0Outlook'), ('174', 'Microsoft\xa0Office\xa0Project'), ('175', 'Microsoft\xa0Office\xa0Access'), ('176', 'Microsoft\xa0Office\xa0Visio'), ('177', 'Microsoft\xa0Office\xa0Sharepoint'), ('178', 'MS\xa0office\xa0applications'), ('179', '1C'), ('180', 'Active\xa0Directory'), ('181', 'Active\xa0Sync'), ('182', 'AD'), ('183', 'Adobe\xa0Acrobat'), ('184', 'Adobe\xa0after\xa0effects'), ('185', 'Adobe\xa0Audition'), ('186', 'Adobe\xa0Photoshop'), ('187', 'Adobe\xa0Premiere\xa0Pro'), ('188', 'Adobe\xa0Reader'), ('189', 'AJAX'), ('190', 'Android\xa0SDK'), ('191', 'Angular'), ('192', 'ANSYS'), ('193', 'Application\xa0Servers'), ('194', 'Arc\xa0GIS'), ('195', 'ArchiCAD'), ('196', 'Ariana'), ('197', 'ASP'), ('198', 'Asterisk'), ('199', 'Asterisk\xa0Server'), ('200', 'ASYCUDA'), ('201', 'AutoCAD'), ('202', 'AutoCAD\xa0Civil\xa03D'), ('203', 'Bootstrap'), ('204', 'Bulk\xa0Rename\xa0utility'), ('205', 'CATIA'), ('206', 'CMS'), ('207', 'Corel'), ('208', 'coreldraw'), ('209', 'Crystal\xa0Report'), ('210', 'CSS'), ('211', 'CSS3'), ('212', 'Data\xa0Deduplication'), ('213', 'Data\xa0warehouse'), ('214', 'Database\xa0performance\xa0tuning'), ('215', 'Devexpress'), ('216', 'DFS'), ('217', 'DHCP'), ('218', 'DNS'), ('219', 'eBudget'), ('220', 'Edge\xa0Server'), ('221', 'eDocument'), ('222', 'eflow'), ('223', 'eHRMS'), ('224', 'EJB\xa03.x'), ('225', 'Entity\xa0Framework'), ('226', 'eTreasury'), ('227', 'EViews'), ('228', 'Exchange'), ('229', 'Exchange\xa0Server'), ('230', 'Exchange(DAG)'), ('231', 'Ext\xa0JS'), ('232', 'extejs'), ('233', 'Fiber\xa0Optics'), ('234', 'Final\xa0Cut\xa0Studio'), ('235', 'Firewall'), ('236', 'Flexsys'), ('237', 'FMG'), ('238', 'FSRM'), ('239', 'FTP'), ('240', 'GeoServer'), ('241', 'Google\xa0Apps\xa0for\xa0Business'), ('242', 'GPO'), ('243', 'GPS'), ('244', 'Group\xa0policy'), ('245', 'Hibernate/JPA'), ('246', 'HTML'), ('247', 'HTML5'), ('248', 'IIS'), ('249', 'illustrator'), ('250', 'InDesign'), ('251', 'IPCC\xa0Inventory\xa0Software'), ('252', 'iSCSI\xa0'), ('253', 'JAVA\xa0EE'), ('254', 'java\xa0SDK'), ('255', 'Java\xa0Spring'), ('256', 'JBoss\xa0Aplication\xa0Server'), ('257', 'JBoss\xa0Seam\xa0Framework'), ('258', 'JMS'), ('259', 'JS'), ('260', 'JSF'), ('261', 'JSON'), ('262', 'Kerio\xa0Operator'), ('263', 'LINQ'), ('264', 'Lumion'), ('265', 'Lync'), ('266', 'Mac\xa0OS'), ('267', 'Magic\xa0X\xa0Audio\xa0Editing'), ('268', 'Magic\xa0X\xa0Music\xa0Macer'), ('269', 'Mail\xa0Server'), ('270', 'Max\xa0MSP'), ('271', 'MAXQDA'), ('272', 'Microsoft\xa0Active\xa0Directory'), ('273', 'Microsoft\xa0Exchange'), ('274', 'Microsoft\xa0Exchange\xa02013-2016'), ('275', 'Microsoft\xa0Exchange\xa0Servers\xa0Clustering'), ('276', 'Microsoft\xa0Expression\xa0Blend'), ('277', 'Microsoft\xa0Project\xa0Server'), ('278', 'Microsoft\xa0SQL\xa0Server\xa0Management\xa0Studio'), ('279', 'Microsoft\xa0Team\xa0Foundation\xa0Server\xa0'), ('280', 'Microsoft\xa0Visual\xa0Studio'), ('281', 'Mozilla\xa0Firefox'), ('282', 'Mplus'), ('283', 'MS\xa0Office\xa0Lync'), ('284', 'MS\xa0SQL'), ('285', 'MS\xa0SQL\xa0Server'), ('286', 'MVC'), ('287', 'MVC\xa0Core'), ('288', 'Mware\xa0vSphere\xa06.x'), ('289', 'Navision'), ('290', 'Network\xa0Administrator\xa0'), ('291', 'NTFS\xa0File\xa0Permission'), ('292', 'NVivo'), ('293', 'OneNote'), ('294', 'OOP'), ('295', 'OOP\xa0PHP'), ('296', 'Oracle'), ('297', 'Oracle\xa011g'), ('298', 'Oracle,\xa0XML'), ('299', 'ORIS'), ('300', 'ORIS\xa0Manager'), ('301', 'Outlook\xa0Anywhere\xa0'), ('302', 'Outlook\xa0Express'), ('303', 'PageMaker'), ('304', 'PDS'), ('305', 'Photoshop'), ('306', 'Power\xa0IP\xa0PBX\xa0Systems'), ('307', 'Premier\xa0Pro'), ('308', 'Project\xa0Server'), ('309', 'Publisher'), ('310', 'RA'), ('311', 'Revit'), ('312', 'RichFaces'), ('313', 'RichFaces/MyFaces'), ('314', 'Routing'), ('315', 'RS.GE'), ('316', 'SCCM'), ('317', 'SCDPM'), ('318', 'SCO'), ('319', 'SCOM'), ('320', 'SCVMM'), ('321', 'Share\xa0Permission'), ('322', 'SharePoint'), ('323', 'Sony\xa0Vegas'), ('324', 'Sound\xa0Forge'), ('325', 'SPSS\xa0Amos'), ('326', 'Stimulsoft'), ('327', 'Switching'), ('328', 'Telerik'), ('329', 'Veritas'), ('330', 'Veritas\xa0Bachup\xa0Exec'), ('331', 'Visio'), ('332', 'Visual\xa0Basic'), ('333', 'Visual\xa0Studio\xa02017'), ('334', 'VLAN'), ('335', 'VOIP'), ('336', 'Voip\xa0Gateways'), ('337', 'VPN'), ('338', 'WDS'), ('339', 'Web\xa0API'), ('340', 'Web\xa0Services'), ('341', 'Web-based\xa0communication'), ('342', 'Windows\xa02016'), ('343', 'Windows\xa07'), ('344', 'Windows\xa0Server'), ('345', 'Windows\xa0server\xa02016\xa0'), ('346', 'Windows\xa0Server\xa02012\xa0R2'), ('347', 'WinForms'), ('348', 'WSUS'), ('349', 'XHTML'), ('350', 'XML'), ('351', '1C\xa0Database'), ('352', 'CISCO\xa0CCNA'), ('353', 'VMware\xa0Server'), ('354', 'Windows\xa0Vista'), ('355', '3D\xa0MAX')], max_length=255, null=True, verbose_name='skills'),
        ),
    ]
