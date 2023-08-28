import { useDropzone } from 'react-dropzone';
import type { FileWithPath } from 'react-dropzone';

import { useUploadThing } from '@/lib/utils/upload-thing';
import { useCallback, useState } from 'react';
import renameFiles from '@/lib/utils/rename-files';
import SuccessToast from './toast';
import { postUrlToFlaskServer } from '@/lib/api/postResumeURL';

const DragAndDrop = () => {
  // states
  const [openToast, setOpenToast] = useState(false);
  const [intro, setIntro] = useState(true);
  const [showRedo, setRedo] = useState(false);
  const [fileToUpload, setFile] = useState<File | null>(null);

  // hooks
  const onDrop = useCallback((acceptedFiles: FileWithPath[]) => {
    setFile(renameFiles(acceptedFiles[0]));
  }, []);

  const { open, isDragActive, getRootProps, getInputProps, acceptedFiles } =
    useDropzone({
      maxFiles: 1,
      noClick: true,
      onDrop: (acceptedFiles) => {
        setIntro(false);
        onDrop(acceptedFiles);
      },
      accept: {
        '.pdf': [],
      },
    });

  const { isUploading, startUpload } = useUploadThing('pdfUploader', {
    onClientUploadComplete: (file) => {
      console.log('uploaded successfully!');
      if (!!file && file.length > 0) {
        console.log(file[0].url);
        // postUrlToFlaskServer(file[0].url);
      }

      setOpenToast(true);
      setFile(null);
      setRedo(true);
    },
    onUploadError: (e) => {
      console.log(e);
      console.error('error occurred while uploading');
    },
    onUploadProgress: (progress: number) => {
      console.log(progress);
    },
  });

  // constants
  const cls =
    'relative flex justify-center items-center flex-col gap-2 w-96 h-52 border-dashed rounded-lg border border-gray-400';
  const btnCls =
    'cursor-pointer bg-C31327A text-white py-1 px-2 rounded-lg text-[12px]';
  const fileName = acceptedFiles[0]?.name;
  const fileSize = acceptedFiles[0]?.size
    ? (acceptedFiles[0]?.size / 8 / 1024).toPrecision(2)
    : 0;

  return (
    <>
      <SuccessToast
        text="Your file has been uploaded"
        open={openToast}
        setOpen={setOpenToast}
      />
      <div {...getRootProps()}>
        <input {...getInputProps()} />

        {isDragActive && !fileToUpload && <div className={cls}>drop here</div>}

        {showRedo && (
          <div
            className={cls}
            onClick={() => {
              setRedo(false);
              setIntro(true);
            }}
          >
            <p>Uploaded</p>
            <button className={btnCls}>Redo..?</button>
          </div>
        )}

        {isUploading && (
          <div className={cls}>
            <p>Uploading</p>
          </div>
        )}

        {!!fileToUpload && !isUploading && (
          <div onClick={() => startUpload([fileToUpload])} className={cls}>
            <p>File: {fileName}</p>
            <p>Size: {fileSize} MBs</p>
            <button className={btnCls} type="button">
              Ready to upload..?
            </button>
          </div>
        )}

        {intro && !isDragActive && (
          <div className={cls}>
            <p>Drag & Drop files here to upload</p>
            <p>or</p>
            <button className={btnCls} type="button" onClick={open}>
              Click to browse Files
            </button>
          </div>
        )}
      </div>
    </>
  );
};

export default DragAndDrop;
