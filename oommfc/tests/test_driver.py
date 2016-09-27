import os
import discretisedfield as df
import oommfc as oc


class TestDriver:
    def setup(self):
        self.system = oc.System(name='test_driver_system')
        mesh = oc.Mesh((0, 0, 0), (10, 10, 10), (1, 1, 2))
        self.system.mesh = mesh
        self.system.hamiltonian += oc.Exchange(1.5e-11)
        self.system.hamiltonian += oc.Demag()
        self.system.dynamics += oc.Precession(2.211e5)
        self.system.dynamics += oc.Damping(1)
        self.system.m = df.Field(mesh, value=(0, 1, 0),
                                 normalisedto=8e5)

    def test_makedir(self):
        driver = oc.Driver()
        driver._makedir(self.system)

        dirname = "{}/".format(self.system.name)
        assert os.path.exists(dirname)

        os.system("rm -r {}".format(dirname))
