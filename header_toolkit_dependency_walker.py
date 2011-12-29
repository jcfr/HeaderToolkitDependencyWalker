#!/usr/bin/python

def extract_headers_directly_included(cpp_source_file):
  """Given a CPP source file, list all directly included headers matching the given pattern."""
  import re
  matches = []
  lines = open(cpp_source_file, "r")
  for line in lines:
    header = re.match("\#include\s+[\"<](.+)[\">]", line)
    if header:
      matches.append(header.group(1))
  return matches

def recursively_list_file_within_directory(directory, pattern):
  """The returned list of file including the relative path to the provided directory."""
  import fnmatch
  import os

  matches = []
  for root, dirnames, filenames in os.walk(directory):
    for filename in fnmatch.filter(filenames, pattern):
      matches.append(os.path.join(root, filename))
  return matches
  
def generate_map_of_header_to_subdirectory(headers_with_relative_path):
  import os
  header_to_subdirectory = {}
  for header in headers_with_relative_path:
    subdirectory = os.path.basename(os.path.dirname(header))
    header_to_subdirectory[os.path.basename(header)] = subdirectory
  return header_to_subdirectory

if __name__ == '__main__':
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option("--toolkit-source-directory", dest="toolkit_source_directory",
                    help="specify the directory containing the source of the toolkit to consider")
  parser.add_option("--project-source-directory", default='.', dest="project_source_directory",
                    help="specify the directory containing the source of the project to process")
  parser.add_option("--toolkit-pattern",
                    dest="toolkit_pattern", default='*.h',
                    help="Pattern used to match toolkit header file")
  parser.add_option("--project-patterns", default='*.h *.cxx *.cpp',
                    dest="project_patterns",
                    help="patterns used to match source files. Example: \"*.h *.cxx *.cpp\"")
  parser.add_option("--verbose",
                    dest="verbose", action="store_true",
                    help="Print verbose information")
  parser.add_option("--extra-verbose",
                    dest="extra_verbose", action="store_true",
                    help="Print extra verbose information")

  (options, args) = parser.parse_args()
  
  requiredArgumentErrorMessage = "argument '%s' is required !"
  if not options.toolkit_source_directory:
    parser.error(requiredArgumentErrorMessage % '--toolkit-source-directory')
  
  if options.extra_verbose: 
    options.verbose = True
  
  import os.path
  options.toolkit_source_directory = os.path.expanduser(options.toolkit_source_directory)
  options.project_source_directory = os.path.expanduser(options.project_source_directory)
 
  toolkit_headers = recursively_list_file_within_directory(options.toolkit_source_directory, options.toolkit_pattern)
  if options.verbose:
    print "%d headers found in [%s] using [%s]" % (len(toolkit_headers), options.toolkit_source_directory, options.toolkit_pattern)
  
  header_to_library_map = generate_map_of_header_to_subdirectory(toolkit_headers)
  if options.verbose:
    print "%d entries added to 'Header -> Library' map " % (len(header_to_library_map.keys()))
  
  expected_libraries = []
  
  all_project_files = []
  project_patterns = options.project_patterns.split(" ")
  for project_pattern in project_patterns:
    project_files = recursively_list_file_within_directory(options.project_source_directory, project_pattern)
    all_project_files.extend(project_files)
    if options.verbose:
      print "Found %s files walking [%s] using [%s] pattern" % (len(project_files), options.project_source_directory, project_pattern)
  
  for filepath in all_project_files:
    project_headers = extract_headers_directly_included(filepath)
    #print "Found %s headers in file [%s]" % (len(project_headers), filepath)
    for header in project_headers:
      if header in header_to_library_map:
        if options.extra_verbose:
          print "[%s] found in [%s]" % (header, header_to_library_map[header])
        expected_libraries.append(header_to_library_map[header])
  
  expected_libraries = sorted(list(set(expected_libraries)))
  for lib in expected_libraries:
    print lib

