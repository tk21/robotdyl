import shutil
import utils


def run(target, outpath, output_directory=False):
    print "Marking the directory as built by the build process"
    utils.mark_as_built(target)

    print "Generating pyo files"
    utils.generate_pyo_files(target)

    print "disabling i18n"
    utils.append_to_local_settings(target, "USE_I18N = False")
    utils.append_to_local_settings(target, "USE_L10N = False")

    print "Disabling DEBUG mode"
    utils.append_to_local_settings(target, "DEBUG = False")

    print "Deleting some blacklisted files"
    utils.delete_blacklisted_files(target)

    print "Collecting static files"
    utils.collectstatic(target)

    print "Deleting extra static files"
    utils.delete_blacklisted_files(target, removejuststatic=True)

    # Django doesn't like deleted py files. Have to investigate more
    # print "Deleting the .py files"
    # utils.delete_py_files(target)

    print "Pregenerating the database"
    utils.generate_db(target)

    print "Adding in a default facility"
    utils.create_default_facility(target)

    # zip up the tmp directory by getting kalite's grandparent
    top_build_directory = target.parent.parent

    outpath = outpath / "ka-lite"
    if output_directory:
        print "Copying built KA Lite to {}".format(outpath)
        shutil.copytree(str(top_build_directory), str(outpath))
    else:
        print "Zipping up everything"
        utils.zip_directory(top_build_directory, out=outpath)
