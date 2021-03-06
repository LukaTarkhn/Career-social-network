from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
from organizations.models import Organization


class Vacancy(models.Model):
    QUALIFICATION = (
        ('1', 'Intern'),
        ('2', 'Junior'),
        ('3', 'Middle'),
        ('4', 'Senior'),
        ('5', 'Lead'),
    )

    TYPE = (
        ('1', 'Full Time'),
        ('2', 'Part Time'),
    )

    SPHERE = (
        ('1', 'Backend'),
        ('2', 'Frontend'),
        ('3', 'Design'),
        ('4', 'Administration'),
        ('5', 'Analytics'),
        ('6', 'Testing'),
        ('7', 'Management'),
        ('8', 'Marketing'),
        ('9', 'Telekom'),
        ('10', 'Sales'),
        ('11', 'Applications'),
        ('12', 'Software'),
        ('13', 'Other'),
    )

    SKILL = (
        ('1', 'ABAP'),
        ('2', 'ActiveMQ'),
        ('3', 'Ada programming'),
        ('4', 'Amazon Web Services'),
        ('5', 'Android'),
        ('6', 'Angular 2+'),
        ('7', 'AngularJS'),
        ('8', 'Ansible'),
        ('9', 'Apache Hive'),
        ('10', 'Apache Kafka'),
        ('11', 'Apache Pig'),
        ('12', 'Apache Spark'),
        ('13', 'ARM'),
        ('14', 'ASP.NET'),
        ('15', 'ASP.NET MVC'),
        ('16', 'Azure'),
        ('17', 'Backbone.js'),
        ('18', 'Bash'),
        ('19', 'Blockchain'),
        ('20', 'C'),
        ('21', 'C#'),
        ('22', 'C++'),
        ('23', 'CakePHP'),
        ('24', 'Cassandra'),
        ('25', 'Chef'),
        ('26', 'Cisco'),
        ('27', 'Clojure'),
        ('28', 'CoffeeScript'),
        ('29', 'Cordova'),
        ('30', 'Cross Platform Mobile'),
        ('31', 'Django'),
        ('32', 'Docker'),
        ('33', 'Drools'),
        ('34', 'Drupal'),
        ('35', 'Elasticsearch'),
        ('36', 'Elixir'),
        ('37', 'ELM'),
        ('38', 'Embedded Linux'),
        ('39', 'Ember.js'),
        ('40', 'Erlang'),
        ('41', 'ETL'),
        ('42', 'Ez Platform'),
        ('43', 'F#'),
        ('44', 'Flash'),
        ('45', 'Flask'),
        ('46', 'Flutter'),
        ('47', 'Fortinet'),
        ('48', 'Fortran'),
        ('49', 'FPGA'),
        ('50', 'Go'),
        ('51', 'Google Cloud Platform'),
        ('52', 'Google Data Studio'),
        ('53', 'Grails'),
        ('54', 'Grape'),
        ('55', 'Groovy'),
        ('56', 'Hadoop'),
        ('57', 'Haskell'),
        ('58', 'HBase'),
        ('59', 'Hibernate'),
        ('60', 'HTML/CSS'),
        ('61', 'Hyper-V'),
        ('62', 'Informatica'),
        ('63', 'Internet of Things'),
        ('64', 'Ionic'),
        ('65', 'iOS'),
        ('66', 'J2EE'),
        ('67', 'Java'),
        ('68', 'JavaFX'),
        ('69', 'JavaScript'),
        ('70', 'Jenkins'),
        ('71', 'Joomla'),
        ('72', 'jQuery'),
        ('73', 'Juniper'),
        ('74', 'Keras'),
        ('75', 'Kotlin'),
        ('76', 'Kubernetes'),
        ('77', 'LAN/WAN'),
        ('78', 'Laravel'),
        ('79', 'Liferay'),
        ('80', 'Linux'),
        ('81', 'Lisp'),
        ('82', 'Looker'),
        ('83', 'Magento'),
        ('84', 'Matlab'),
        ('85', 'Memcached'),
        ('86', 'Meteor'),
        ('87', 'MongoDB'),
        ('88', 'MySQL'),
        ('89', '.NET'),
        ('90', '.NET Core'),
        ('91', 'NLP'),
        ('92', 'Node.js'),
        ('93', 'Objective-C'),
        ('94', 'OCaml'),
        ('95', 'OpenGL'),
        ('96', 'OpenStack'),
        ('97', 'Oracle Database'),
        ('98', 'Pandas'),
        ('99', 'Pentaho'),
        ('100', 'Perl'),
        ('101', 'PHP'),
        ('102', 'Pixi.js'),
        ('103', 'Play'),
        ('104', 'PL/SQL'),
        ('105', 'Polymer'),
        ('106', 'PostgreSQL'),
        ('107', 'Power BI'),
        ('108', 'Prestashop'),
        ('109', 'Proxmox Virtual Environment'),
        ('110', 'Puppet'),
        ('111', 'Python'),
        ('112', 'Pytorch'),
        ('113', 'Qlik'),
        ('114', 'Qt'),
        ('115', 'R'),
        ('116', 'RabbitMQ'),
        ('117', 'ReactJS'),
        ('118', 'React Native'),
        ('119', 'Redis'),
        ('120', 'Redux'),
        ('121', 'Riot.js'),
        ('122', 'Ruby'),
        ('123', 'Ruby on Rails'),
        ('124', 'Rust'),
        ('125', 'SAS'),
        ('126', 'SASS'),
        ('127', 'Scala'),
        ('128', 'Scheme'),
        ('129', 'scikit-learn'),
        ('130', 'Selenium'),
        ('131', 'SEO'),
        ('132', 'Shopware'),
        ('133', 'Sinatra'),
        ('134', 'Solr'),
        ('135', 'Spring'),
        ('136', 'Spring Boot'),
        ('137', 'SPSS'),
        ('138', 'SQL'),
        ('139', 'SQL Server'),
        ('140', 'Stata'),
        ('141', 'Struts'),
        ('142', 'Swift'),
        ('143', 'Symfony'),
        ('144', 'Tableau'),
        ('145', 'Talend'),
        ('146', 'TCL'),
        ('147', 'TensorFlow'),
        ('148', 'Terraform'),
        ('149', 'Tomcat'),
        ('150', 'T-SQL'),
        ('151', 'TypeScript'),
        ('152', 'Unity'),
        ('153', 'Unix Shell Scripting'),
        ('154', 'VBA'),
        ('155', 'VB.NET'),
        ('156', 'Verilog'),
        ('157', 'VHDL'),
        ('158', 'VMWare vSphere'),
        ('159', 'Vue.js'),
        ('160', 'VxWorks'),
        ('161', 'WCF'),
        ('162', 'Windows'),
        ('163', 'Windows Mobile'),
        ('164', 'WordPress'),
        ('165', 'WPF'),
        ('166', 'x86 Assembly'),
        ('167', 'Xamarin'),
        ('168', 'Yii'),
        ('169', 'Zend Framework'),
        ('170', 'Microsoft Office Word'),
        ('171', 'Microsoft Office Excel'),
        ('172', 'Microsoft Office PowerPoint'),
        ('173', 'Microsoft Office Outlook'),
        ('174', 'Microsoft Office Project'),
        ('175', 'Microsoft Office Access'),
        ('176', 'Microsoft Office Visio'),
        ('177', 'Microsoft Office Sharepoint'),
        ('178', 'MS office applications'),
        ('179', '1C'),
        ('180', 'Active Directory'),
        ('181', 'Active Sync'),
        ('182', 'AD'),
        ('183', 'Adobe Acrobat'),
        ('184', 'Adobe after effects'),
        ('185', 'Adobe Audition'),
        ('186', 'Adobe Photoshop'),
        ('187', 'Adobe Premiere Pro'),
        ('188', 'Adobe Reader'),
        ('189', 'AJAX'),
        ('190', 'Android SDK'),
        ('191', 'Angular'),
        ('192', 'ANSYS'),
        ('193', 'Application Servers'),
        ('194', 'Arc GIS'),
        ('195', 'ArchiCAD'),
        ('196', 'Ariana'),
        ('197', 'ASP'),
        ('198', 'Asterisk'),
        ('199', 'Asterisk Server'),
        ('200', 'ASYCUDA'),
        ('201', 'AutoCAD'),
        ('202', 'AutoCAD Civil 3D'),
        ('203', 'Bootstrap'),
        ('204', 'Bulk Rename utility'),
        ('205', 'CATIA'),
        ('206', 'CMS'),
        ('207', 'Corel'),
        ('208', 'coreldraw'),
        ('209', 'Crystal Report'),
        ('210', 'CSS'),
        ('211', 'CSS3'),
        ('212', 'Data Deduplication'),
        ('213', 'Data warehouse'),
        ('214', 'Database performance tuning'),
        ('215', 'Devexpress'),
        ('216', 'DFS'),
        ('217', 'DHCP'),
        ('218', 'DNS'),
        ('219', 'eBudget'),
        ('220', 'Edge Server'),
        ('221', 'eDocument'),
        ('222', 'eflow'),
        ('223', 'eHRMS'),
        ('224', 'EJB 3.x'),
        ('225', 'Entity Framework'),
        ('226', 'eTreasury'),
        ('227', 'EViews'),
        ('228', 'Exchange'),
        ('229', 'Exchange Server'),
        ('230', 'Exchange(DAG)'),
        ('231', 'Ext JS'),
        ('232', 'extejs'),
        ('233', 'Fiber Optics'),
        ('234', 'Final Cut Studio'),
        ('235', 'Firewall'),
        ('236', 'Flexsys'),
        ('237', 'FMG'),
        ('238', 'FSRM'),
        ('239', 'FTP'),
        ('240', 'GeoServer'),
        ('241', 'Google Apps for Business'),
        ('242', 'GPO'),
        ('243', 'GPS'),
        ('244', 'Group policy'),
        ('245', 'Hibernate/JPA'),
        ('246', 'HTML'),
        ('247', 'HTML5'),
        ('248', 'IIS'),
        ('249', 'illustrator'),
        ('250', 'InDesign'),
        ('251', 'IPCC Inventory Software'),
        ('252', 'iSCSI '),
        ('253', 'JAVA EE'),
        ('254', 'java SDK'),
        ('255', 'Java Spring'),
        ('256', 'JBoss Aplication Server'),
        ('257', 'JBoss Seam Framework'),
        ('258', 'JMS'),
        ('259', 'JS'),
        ('260', 'JSF'),
        ('261', 'JSON'),
        ('262', 'Kerio Operator'),
        ('263', 'LINQ'),
        ('264', 'Lumion'),
        ('265', 'Lync'),
        ('266', 'Mac OS'),
        ('267', 'Magic X Audio Editing'),
        ('268', 'Magic X Music Macer'),
        ('269', 'Mail Server'),
        ('270', 'Max MSP'),
        ('271', 'MAXQDA'),
        ('272', 'Microsoft Active Directory'),
        ('273', 'Microsoft Exchange'),
        ('274', 'Microsoft Exchange 2013-2016'),
        ('275', 'Microsoft Exchange Servers Clustering'),
        ('276', 'Microsoft Expression Blend'),
        ('277', 'Microsoft Project Server'),
        ('278', 'Microsoft SQL Server Management Studio'),
        ('279', 'Microsoft Team Foundation Server '),
        ('280', 'Microsoft Visual Studio'),
        ('281', 'Mozilla Firefox'),
        ('282', 'Mplus'),
        ('283', 'MS Office Lync'),
        ('284', 'MS SQL'),
        ('285', 'MS SQL Server'),
        ('286', 'MVC'),
        ('287', 'MVC Core'),
        ('288', 'Mware vSphere 6.x'),
        ('289', 'Navision'),
        ('290', 'Network Administrator '),
        ('291', 'NTFS File Permission'),
        ('292', 'NVivo'),
        ('293', 'OneNote'),
        ('294', 'OOP'),
        ('295', 'OOP PHP'),
        ('296', 'Oracle'),
        ('297', 'Oracle 11g'),
        ('298', 'Oracle, XML'),
        ('299', 'ORIS'),
        ('300', 'ORIS Manager'),
        ('301', 'Outlook Anywhere '),
        ('302', 'Outlook Express'),
        ('303', 'PageMaker'),
        ('304', 'PDS'),
        ('305', 'Photoshop'),
        ('306', 'Power IP PBX Systems'),
        ('307', 'Premier Pro'),
        ('308', 'Project Server'),
        ('309', 'Publisher'),
        ('310', 'RA'),
        ('311', 'Revit'),
        ('312', 'RichFaces'),
        ('313', 'RichFaces/MyFaces'),
        ('314', 'Routing'),
        ('315', 'RS.GE'),
        ('316', 'SCCM'),
        ('317', 'SCDPM'),
        ('318', 'SCO'),
        ('319', 'SCOM'),
        ('320', 'SCVMM'),
        ('321', 'Share Permission'),
        ('322', 'SharePoint'),
        ('323', 'Sony Vegas'),
        ('324', 'Sound Forge'),
        ('325', 'SPSS Amos'),
        ('326', 'Stimulsoft'),
        ('327', 'Switching'),
        ('328', 'Telerik'),
        ('329', 'Veritas'),
        ('330', 'Veritas Bachup Exec'),
        ('331', 'Visio'),
        ('332', 'Visual Basic'),
        ('333', 'Visual Studio 2017'),
        ('334', 'VLAN'),
        ('335', 'VOIP'),
        ('336', 'Voip Gateways'),
        ('337', 'VPN'),
        ('338', 'WDS'),
        ('339', 'Web API'),
        ('340', 'Web Services'),
        ('341', 'Web-based communication'),
        ('342', 'Windows 2016'),
        ('343', 'Windows 7'),
        ('344', 'Windows Server'),
        ('345', 'Windows server 2016 '),
        ('346', 'Windows Server 2012 R2'),
        ('347', 'WinForms'),
        ('348', 'WSUS'),
        ('349', 'XHTML'),
        ('350', 'XML'),
        ('351', '1C Database'),
        ('352', 'CISCO CCNA'),
        ('353', 'VMware Server'),
        ('354', 'Windows Vista'),
        ('355', '3D MAX')
    )

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    url = models.CharField(verbose_name='Url field', max_length=30, unique=True)
    title = models.CharField(verbose_name='Vacancy title', max_length=150, null=True)
    qualification = models.CharField(verbose_name='Qualification', max_length=10, null=True, choices=QUALIFICATION)
    salary = models.IntegerField(verbose_name='Salary', null=True, blank=True)
    location = models.CharField(verbose_name='Location', max_length=80, null=True, blank=True)
    work_type = models.CharField(verbose_name='Work type', max_length=15, null=True, choices=TYPE, default='1')
    remote_work = models.BooleanField(verbose_name='Remote work', default=False)
    description = models.TextField(verbose_name='Description', max_length=4000, null=True)
    bonuses = models.TextField(verbose_name='Bonuses', max_length=1500, null=True, blank=True)
    instructions = models.TextField(verbose_name='Instructions', max_length=1500, null=True, blank=True)
    sphere = MultiSelectField(choices=SPHERE, max_choices=2, max_length=20, verbose_name='Sphere', null=True)
    skills = MultiSelectField(choices=SKILL, max_choices=12, max_length=30, verbose_name='skills', null=True)
    date_created = models.DateTimeField(verbose_name='Create date', auto_now_add=True)

    def __str__(self):
        return str(self.title)


class VacancyResponse(models.Model):
    STATUS = (
        ('1', 'Submitted'),
        ('2', 'Accepted'),
        ('3', 'Marked'),
        ('4', 'Declined'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True)
    description = models.TextField(verbose_name='Description', max_length=500, null=True, blank=True)
    status = models.CharField(verbose_name='Status', max_length=10, choices=STATUS, default='1')
    date_created = models.DateTimeField(verbose_name='Create date', auto_now_add=True)

    def __str__(self):
        return str(self.vacancy)

