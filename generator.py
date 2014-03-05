__author__ = 'Ameen Tayyebi'


class Generator:

    output_file_path = ""
    module_name = ""
    preprocessed_classes = []

    def __init__(self, preprocessed_classes, output_file_path, module_name):
        self.output_file_path = output_file_path
        self.module_name = module_name
        self.preprocessed_classes = preprocessed_classes

    def write(self):

        # Open output file
        output_file = open(self.output_file_path, 'w')

        self.write_module(output_file)

        # Close the output file
        output_file.close()

    def write_module(self, output_file):

        # Write module declaration
        if self.module_name != '':
            output_file.write('declare module %s {\r\n' % self.module_name)

        # Process all classes
        for cls in self.preprocessed_classes:
            self.write_class(cls, output_file)

        if self.module_name != "":
            output_file.write("}\r\n")

    def write_class(self, cls, output_file):

        output_file.write('\texport class %s {\r\n' % cls['name'])

        # Generate methods
        for method in cls['methods']['public']:

            # Ignore destructors
            if method['destructor']:
                continue

            # Generate list of parameters
            param_list = ','.join('%s:%s' % (arg['name'], arg['type']) for arg in method['parameters'])

            # Print composed signature
            if method['constructor']:
                output_file.write('\t\tconstructor(%s);\r\n' % param_list)
            else:
                output_file.write('\t\tpublic %s(%s):%s;\r\n' % (method['name'], param_list, method['rtnType']))

        output_file.write('\t}\r\n')
