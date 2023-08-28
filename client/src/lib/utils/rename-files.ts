import crypto from 'crypto';

const renameFiles = (originalFile: File) => {
  if (!originalFile) return null;
  const newFileName = `file_${generateShortHash(originalFile.name)}.pdf`;
  const blob = new Blob([originalFile], { type: originalFile.type });
  const renamedFile = new File([blob], newFileName, {
    type: originalFile.type,
  });
  return renamedFile;
};

function generateShortHash(input: string): string {
  const hash = crypto.createHash('md5').update(input).digest('hex');
  const shortHash = hash.substring(0, 6);
  return shortHash;
}

export default renameFiles;
