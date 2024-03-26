import LinearWithValueLabel from '@/app/components/linear-progress';
import CircularIndeterminate from '@/app/components/circular-indeterminate';

export default function page(){
    return (
        <div>
            <p className="text-xl">Execution</p>
            <LinearWithValueLabel />
            <CircularIndeterminate />
        </div>
    );
}