#!/usr/bin/env python
# -*- coding:utf-8 -*-

#./autobuild.py -p youproject.xcodeproj -s schemename
#./autobuild.py -w youproject.xcworkspace -s schemename

import argparse
import subprocess
import os

#configuration for iOS build setting

CONFIGURATION = "Debug";
EXPORT_OPTIONS_PLIST = "exOptions.plist";
#会在桌面创建输出ipa文件的目录
EXPORT_MAIN_DIRECTORY=os.path.join(os.path.expanduser("~"), 'Desktop')+os.path.sep;


def cleanArchiveFile(archiveFile):
	cleanCmd = "rm -r %s" %(archiveFile)
	process = subprocess.Popen(cleanCmd, shell = True)
	process.wait()
	print "cleaned archiveFile: %s" %(archiveFile)


def getIpaPath(exportPath):
	cmd = "ls %s" %(exportPath)
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	(stdoutdata, stderrdata) = process.communicate()
	ipaName = stdoutdata.strip()
	ipaPath = exportPath + "/" + ipaName
	return ipaPath

###########################################################################
#step1 生成 .xcarchive
def buildArchivePath(tempName):
	process = subprocess.Popen("pwd", stdout=subprocess.PIPE)
	(stdoutdata, stderrdata) = process.communicate()
	archiveName = "%s.xcarchive" %(tempName)
	archivePath = stdoutdata.strip() + '/' + archiveName
	return archivePath

#创建输出ipa文件路径: ~/Desktop/{scheme}{2016-12-28_08-08-10}
def buildExportDirectory(kscheme):
	dateCmd = 'date "+%Y-%m-%d_%H-%M-%S"'
	process = subprocess.Popen(dateCmd, stdout=subprocess.PIPE, shell=True)
	(stdoutdata, stderrdata) = process.communicate()
	exportDirectory = "%s%s%s" %(EXPORT_MAIN_DIRECTORY, kscheme, stdoutdata.strip())
	return exportDirectory

#step1 导出.ipa
def exportArchive(kscheme, archivePath):
	exportDirectory = buildExportDirectory(kscheme)
	print "exportDirectory:",exportDirectory;
	exportCmd = "xcodebuild -exportArchive -archivePath %s -exportPath %s  -exportOptionsPlist %s" %(archivePath, exportDirectory, EXPORT_OPTIONS_PLIST)
	process = subprocess.Popen(exportCmd, shell=True)
	(stdoutdata, stderrdata) = process.communicate()

	signReturnCode = process.returncode
	if signReturnCode != 0:
		print "export %s failed" %(kscheme)
		#return ""
	else:
		print "export %s success" %(kscheme)
		#return exportDirectory
###########################################################################

#cocopod打包	；
def buildWorkspace(kworkspace, kscheme):
	archivePath = buildArchivePath(kscheme)
	print "archivePath: " + archivePath
	archiveCmd = 'xcodebuild -workspace %s -scheme %s -configuration %s archive -archivePath %s -destination generic/platform=iOS' %(kworkspace, kscheme, CONFIGURATION, archivePath)
	process = subprocess.Popen(archiveCmd, shell=True)
	process.wait()

	archiveReturnCode = process.returncode
	if archiveReturnCode != 0:
		print "archive workspace %s failed" %(kworkspace)
		cleanArchiveFile(archivePath)
	else:
		#exportDirectory =exportArchive(kscheme, archivePath)
		exportArchive(kscheme, archivePath)
		cleanArchiveFile(archivePath)
		# if exportDirectory != "":
		# 	ipaPath = getIpaPath(exportDirectory)
		# 	#uploadIpaToPgyer(ipaPath)

#普通project打包	；
def buildProject(kproject, kscheme):
	archivePath = buildArchivePath(kscheme)
	print "archivePath: " + archivePath
	archiveCmd = 'xcodebuild -project %s -scheme %s -configuration %s archive -archivePath %s -destination generic/platform=iOS build' \
			   %(kproject, kscheme, CONFIGURATION, archivePath);
	process = subprocess.Popen(archiveCmd, shell=True)
	process.wait()

	archiveReturnCode = process.returncode
	if archiveReturnCode != 0:
		print "archive workspace failed";
		cleanArchiveFile(archivePath)
	else:
		#exportDirectory = exportArchive(kscheme, archivePath);
		exportArchive(kscheme, archivePath);
		print "archive workspace success: \n";
		cleanArchiveFile(archivePath)
		# if exportDirectory != "":
		# 	ipaPath = getIpaPath(exportDirectory)



def xcbuild(options):
    # project_path = EXPORT_MAIN_DIRECTORY +'agoraFile.txt';
    # channelCodeList=[];
    # f = open(project_path);
    # channel_list = f.readlines();
    # f.close()
    # # 遍历渠道列表
    # for channel in channel_list:
    #      # 删除换行符
    #     channel = channel.strip();
    #     channelCodeList.append(channel);
	project = '/Users/changku/Desktop/SgmjzGame/SgmjzGame.xcodeproj';
	scheme = os.path.splitext(os.path.split(project)[1])[0];
	# project = options.project
	workspace = options.workspace
	# scheme = options.scheme;
	#如果选择东西为空跳过；
	if project is None and workspace is None:
		pass;
	# 如果普通project为空跳过；
	elif project is not None:
		buildProject(project, scheme)
	# 如果workspace为空跳过；
	elif workspace is not None:
		buildWorkspace(workspace, scheme)

def main():
	parser = argparse.ArgumentParser()
	#cocopod打包
	parser.add_argument("-w", "--workspace", help="Build the workspace name.xcworkspace.", metavar="name.xcworkspace")
	# 普通打包
	parser.add_argument("-p", "--project", help="Build the project name.xcodeproj.", metavar="name.xcodeproj")
	# 输入schemename
	parser.add_argument("-s", "--scheme", help="Build the scheme specified by schemename. Required if building a workspace.", metavar="schemename")
	options = parser.parse_args()
	print "options: %s" % (options)
	xcbuild(options)

if __name__ == '__main__':
	main()
