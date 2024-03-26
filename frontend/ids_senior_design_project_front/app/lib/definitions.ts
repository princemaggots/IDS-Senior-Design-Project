export type BaseInputProps = {
    label: string;
};

export type SelectInputProps = BaseInputProps & {
    values: string[];
};

export type CheckInputProps = BaseInputProps;

export type NumberInputProps = BaseInputProps & {
    min: number;
    max: number;
    step: number;
    defaultValue: number;
};

export type LinerProgressProp = {
    value: number;
};