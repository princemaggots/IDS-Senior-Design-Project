'use client'

import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogTitle from '@mui/material/DialogTitle';
import Paper from '@mui/material/Paper';
import { useState } from 'react';
import Draggable from 'react-draggable';

type ConfirmButtonProp = {
    text: string;
    className?: string;
    prompt: string;
    href: string;
}

function PaperComponent(props: any) {
    return (
        <Draggable
        handle="#draggable-dialog-title"
        cancel={'[class*="MuiDialogContent-root"]'}
        >
            <Paper {...props} />
        </Draggable>
    );
}

export default function ConfirmButton({ text, className, prompt, href }: ConfirmButtonProp) {
    const [open, setOpen] = useState(false);

    const handleOpen = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault()
        setOpen((prevState) => !prevState);
    };

    return (
        <>
            <Button className={className} variant='outlined' onClick={handleOpen}>{text}</Button>
            <Dialog
                open={open}
                onClose={handleOpen}
                PaperComponent={PaperComponent}
                aria-labelledby="draggable-dialog-title"
            >
                <DialogTitle style={{ cursor: 'move' }} id="draggable-dialog-title">
                    {prompt}
                </DialogTitle>
                <DialogActions className='flex justify-evenly'>
                    <Button autoFocus variant='outlined' onClick={handleOpen}>
                        Cancel
                    </Button>
                    <Button autoFocus variant='contained' className='bg-primary' href={href} onClick={handleOpen}>
                        Discard
                    </Button>
                </DialogActions>
            </Dialog>
        </>
    );
}